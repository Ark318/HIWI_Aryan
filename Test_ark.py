import glob
import os
import sys
import time
import math
import numpy as np
import subprocess
from datetime import datetime

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
#import generate_traffic
import argparse
import logging
import random
import pygame
from carla import VehicleAckermannControl


def main():
    argparser = argparse.ArgumentParser(
        description=__doc__)
    argparser.add_argument(
        '--host',
        metavar='H',
        default='127.0.0.1',
        help='IP of the host server (default: 127.0.0.1)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    args = argparser.parse_args()

    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
    
    client = carla.Client(args.host, args.port)
    client.set_timeout(100.0)

      
    try:
               
       # Define the range of values for steering angles, velocities
        Start_steer_angles = [0, 45]  
        End_steer_angles = [0, 45]
        Start_velocity = [0, 25]
        End_velocities = [0, 7] 
       

        # Iterate over each combination of parameters
        for ivelocity in Start_velocity:
            for velocity in End_velocities: 
                if End_steer_angles >= Start_steer_angles:
                    for iangle in Start_steer_angles:
                        for angle in End_steer_angles:
                            
                            # Generate timestamp for log file naming    
                            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")    
                            # Logfile naming with timestamp
                            Logfile = open(f'/home/inderst/KICSAFe/KICSAFe_Test/Logs/Test_pos_{timestamp}.txt', 'w')
                            Logfile.write("New Test\n")
                            Logfile_2 = open(f'/home/inderst/KICSAFe/KICSAFe_Test/Logs/Test_vel_{timestamp}.txt', 'w')
                            Logfile_2.write("New Test\n")
                            Logfile_3 = open(f'/home/inderst/KICSAFe/KICSAFe_Test/Logs/Test_accel_{timestamp}.txt', 'w')
                            Logfile_3.write("New Test\n")
                        
                        
                        
                            # Initialise    
                            world = client.get_world()
                            map = world.get_map()
                            blueprint_library = world.get_blueprint_library()
                            map = map.name
                            ego_vehicle = None
                            ego_cam = None
                            collision_sensor = None
                            collision_occurred = False
                            ego_lane = None
                            ego_obs = None
                            ego_gnss = None
                            imu_sensor = None
                            actor_list = world.get_actors()
                            

                            # # Load world
                            # world = client.load_world('Town05_Opt')

                            # # Toggle all buildings off
                            # world.unload_map_layer(carla.MapLayer.Buildings)
                            map_choosen = "Town05"
                            if map_choosen in map:
                                world = client.reload_world()
                            else:
                                world = client.load_world(map_choosen)
                            
                            settings = world.get_settings()
                            settings.fixed_delta_seconds = 0.02
                            # settings.substepping = True
                            # settings.max_substep_delta_time = 0.01
                            # settings.max_substeps = 10
                            world.apply_settings(settings)
                            client.reload_world(False) # reload map keeping the world settings
 

                            # Spawn ego vehicle
                            ego_bp = blueprint_library.find('vehicle.audi.etron')
                            ego_bp.set_attribute('role_name','ego')
                            print('\nEgo role_name is set')
                            ego_color = random.choice(ego_bp.get_attribute('color').recommended_values)
                            ego_bp.set_attribute('color',ego_color)
                            print('\nEgo color is set')
                            
                            spawn_points = world.get_map().get_spawn_points()
                            number_of_spawn_points = len(spawn_points)

                            
                            if 0 < number_of_spawn_points:
                                # random.shuffle(spawn_points)
                                ego_transform = spawn_points[22]
                                spawn_points = carla.Transform()
                                ego_vehicle = world.try_spawn_actor(ego_bp,ego_transform)
                                print('\nEgo is spawned')
                            else: 
                                logging.warning('Could not found any spawn points')
                        
                            # ==============================================================================
                            # --spectator --------------------------------------------
                            # ==============================================================================
                            
                            spectator = world.get_spectator()
                            world_snapshot = world.wait_for_tick() 
                            transform = carla.Transform(ego_vehicle.get_transform().transform(carla.Location(x=-8,z=3)),ego_vehicle.get_transform().rotation)
                            spectator.set_transform(transform)
                            
                            ego_global= ego_vehicle.get_transform()
                            ego_global_location = ego_global.location
                            ego_global_rotation = ego_global.rotation
                            print(f"Vehicle Location: {ego_global_location}")
                            print(f"Vehicle Rotation: {ego_global_rotation}") 
                            yaw = math.radians(ego_global_rotation.yaw)
                            print(f"Yaw (in radians): {yaw}")
                            rotation_matrix = np.array([
                                [math.cos(yaw), math.sin(yaw)],
                                [-math.sin(yaw), math.cos(yaw)]
                            ])  
                            Line = [f" Start_velocity[kmph]-{ivelocity :<20} End_Velocity[m/s]-{velocity :<20} Start_angle-{iangle :<20} End_angle-{angle :<20}\n {'X':<20} {'Y':<20} {'Z':<20} {'Time':<20}\n"]
                            Logfile.writelines(Line)
                            Line = [f"Start_velocity[kmph]-{ivelocity :<20} End_Velocity[m/s]-{velocity :<20} Start_angle-{iangle :<20} End_angle-{angle :<20}\n {'X':<20} {'Y':<20} {'Z':<20} {'Time':<20} \n"]
                            Logfile_2.writelines(Line)
                            Line = [f"Start_velocity[kmph]-{ivelocity:<20} End_Velocity([/s)]{velocity :<20} Start_angle-{iangle :<20} End_angle-{angle :<20}\n {'X':<20} {'Y':<20} {'Z':<20} {'Time':<20} \n"]
                            Logfile_3.writelines(Line)
                            
                            
                            
                            
                                      
                            # ==============================================================================
                            # --collision sensor --------------------------------------------
                            # ==============================================================================
                            
                            col_bp = blueprint_library.find('sensor.other.collision')
                            col_location = carla.Location(x=0, y=0, z=2)  # Adjust according to the vehicle dimensions
                            col_rotation = carla.Rotation(pitch=0, yaw=0, roll=0)
                            col_transform = carla.Transform(col_location, col_rotation)
                            collision_sensor = world.spawn_actor(col_bp, col_transform, attach_to=ego_vehicle, attachment_type=carla.AttachmentType.Rigid)

                            def on_collision(event):
                                global collision_occurred
                                collision_occurred = True
                                other_actor = event.other_actor
                                print(f"Collision detected with {other_actor.type_id}")
                            collision_sensor.listen(on_collision)


                            # ==============================================================================
                            # --IMU sensor --------------------------------------------
                            # ==============================================================================
                            
                            imu_bp = blueprint_library.find('sensor.other.imu')
                            imu_location = carla.Location(x=0, y=0, z=2)  # Adjust according to the vehicle dimensions
                            imu_rotation = carla.Rotation(pitch=0, yaw=0, roll=0)
                            imu_transform = carla.Transform(imu_location, imu_rotation)
                            imu_bp.set_attribute("sensor_tick",str(0.02))
                            imu_sensor = world.spawn_actor(imu_bp, imu_transform, attach_to=ego_vehicle, attachment_type=carla.AttachmentType.Rigid)

                            def on_imu_measurement(imu_data):
                                # acceleration = imu_data.accelerometer
                                # print(f"IMU Data: Acceleration = {acceleration}")
                                formatted_line = [f"{imu_data.accelerometer.x:<20.2f} {imu_data.accelerometer.y:<20.2f} {imu_data.accelerometer.z:<20.2f} {elapsed_time:<20.2f}\n"] 
                                Logfile_3.writelines(formatted_line)
                            # imu_sensor.listen(on_imu_measurement)
                            imu_sensor.listen(lambda imu_data: on_imu_measurement(imu_data))

                            # ==============================================================================
                            # --Formating--------------------------------------------
                            # ==============================================================================

                            

                            

                            # ==============================================================================
                            # --Test Controls--------------------------------------------
                            # ==============================================================================
                                        
                            # # Set the control parameters for the ego vehicle
                            # control = carla.VehicleControl()
                            # control.steer = angle
                            # ego_vehicle.apply_control(control)
                            # # ego_vehicle.set_desired_velocity(carla.Vector3D(-(ivelocity/3.6), 0, 0))
                            
                            ackermann_control = carla.VehicleAckermannControl()
                            ackermann_control.steer = np.radians(iangle)
                            ego_vehicle.apply_ackermann_control(ackermann_control)
                            
                            ego_vehicle.set_target_velocity(carla.Vector3D(-(ivelocity / 3.6), 0, 0))  # Convert velocity to m/s
                            # test_physics = ego_vehicle.get_physics_control()
                            
                            
                            # ackermann_control = carla.VehicleAckermannControl()
                            # ackermann_control.steer = np.radians(angle)
                            # ackermann_control.steer_speed = 0.1
                            # ackermann_control.speed = velocity/3.6 
                            
                        
                        
                            # ==============================================================================
                            # --Simulation run time--------------------------------------------
                            # ==============================================================================                    
                            # Simulation clock
                            SIMULATION_DURATION = 5
                            start_time = world.get_snapshot().timestamp.elapsed_seconds

                    
                            # ==============================================================================
                            # --Loop for simulation--------------------------------------------
                            # ==============================================================================
                                            
                            while not collision_occurred and world.get_snapshot().timestamp.elapsed_seconds - start_time < SIMULATION_DURATION:
                                world.tick()
                                # Measure elapsed time
                                elapsed_time = world.get_snapshot().timestamp.elapsed_seconds - start_time
                                if elapsed_time >= 5:
                                    break    
                                ackermann_control = VehicleAckermannControl(
                                steer= np.radians(-angle),            # Steer to the right (positive value)
                                steer_speed=1,      # Moderate steering velocity
                                speed= velocity,           # Desired speed of m/s
                                acceleration= 0.0,     # Desired acceleration of m/s^2
                                jerk=0.0              # No specific jerk 
                                )
                                ego_vehicle.apply_ackermann_control(ackermann_control)
                                    
                                # --------------
                                # Add Test sensor to ego vehicle. 
                                test_sensor_pos = ego_vehicle.get_location()
                                test_sensor_vel = ego_vehicle.get_velocity()
                                test_sensor_accel = ego_vehicle.get_acceleration()
                                
                                # --------------
                                # tansform
                                relative_position = carla.Location(
                                    ego_global_location.x - test_sensor_pos.x,
                                    ego_global_location.y - test_sensor_pos.y,
                                )
                                
                                relative_position_np = np.array([relative_position.x, relative_position.y])
                                local_position_np = np.dot(rotation_matrix, relative_position_np)

                                local_position = carla.Location(x=local_position_np[0], y=local_position_np[1])
                                
                                print(f"Global Position: {test_sensor_pos}, Local Position: {local_position}")
                                
                                
                                # --------------
                                # print logs
                                print("test sensor measure pos: "+str(test_sensor_pos)+" delta time: "+str(elapsed_time)+'\n')
                                print("test sensor measure vel: "+str(test_sensor_vel)+" delta time: "+str(elapsed_time)+'\n')
                                # print("test sensor measure accel: "+str(test_sensor_accel)+" delta time: "+str(elapsed_time)+'\n')
                                # --------------
                                # write data into the logs files 
                                formatted_line = [f"{local_position.x:<20.2f} {local_position.y:<20.2f} {local_position.z:<20.2f} {elapsed_time:<20.2f}\n"]
                                Logfile.writelines(formatted_line)
                                formatted_line = [f"{test_sensor_vel.x:<20.2f} {test_sensor_vel.y:<20.2f} {test_sensor_vel.z:<20.2f} {elapsed_time:<20.2f}\n"]
                                Logfile_2.writelines(formatted_line)
                                # formatted_line = [f"{test_sensor_accel.x:<20.2f} {test_sensor_accel.y:<20.2f} {test_sensor_accel.z:<20.2f} {elapsed_time:<20.2f}\n"]
                                # Logfile_3.writelines(formatted_line)
                        
            
    finally:
        for actor in actor_list:
            actor.destroy()
            print("terminated")
        # --------------
        # Stop recording and destroy actors
        # --------------
        Logfile.close()
        Logfile_2.close()
        Logfile_3.close()
        client.stop_recorder()
        if ego_vehicle is not None:
            if ego_cam is not None:
                ego_cam.stop()
                ego_cam.destroy()
            if collision_sensor is not None:
                collision_sensor.stop()
                collision_sensor.destroy()
            if ego_lane is not None:
                ego_lane.stop()
                ego_lane.destroy()
            if ego_obs is not None:
                ego_obs.stop()
                ego_obs.destroy()
            if ego_gnss is not None:
                ego_gnss.stop()
                ego_gnss.destroy()
            if imu_sensor is not None:
                imu_sensor.stop()
                imu_sensor.destroy()
            ego_vehicle.destroy()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('\nDone with test.py.')
        
# while True:
    # transform = vehicle.get_transform()
    # yaw = transform.rotation.yaw
    # print(f'Vehicle Yaw: {yaw:.2f} degrees')