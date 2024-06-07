
cmenv;

% folder path
Scenario_list_path = 'C:\Users\ark8318\CM_Projects\SimOutput\ei702-15-16\20240404';

%a list of all files and folders in this folder
files = dir(Scenario_list_path);

%only the filenames (excluding folders)
fileNames = {files(~[files.isdir]).name};


% sortedfilenames = sort(fileNames, 'numeric');

% % % % % % %  Get the time modified for each file
% % % % % % fileTimes = [files(~[files.isdir]).datenum];
% % % % % % 
% % % % % % %  Sort based on time modified
% % % % % % [~, sortedIndices] = sort(fileTimes);
% % % % % % sortedFileNames = fileNames(sortedIndices);
% % % % % % 
% % % % % %  % fileList = cell(length(sortedFileNames), 1);
% % % % % % % Initialize
% % % % % % Scenario_list = {};
% % % % % % 
% % % % % % % Filter files with '.erg' extension
% % % % % % for i = 1:length(fileNames)
% % % % % %     if endsWith(fileNames{i}, '.erg')
% % % % % %         Scenario_list{end+1} = fullfile(Scenario_list_path, fileNames{i});
% % % % % %     end
% % % % % % end 


% Initialize
Scenario_list = {};

% Filter files with '.erg' extension
for i = 1:length(fileNames)
    if endsWith(fileNames{i}, '.erg')
        Scenario_list{end+1} = fullfile(Scenario_list_path, fileNames{i});
    end
end 
% % % % % % fileTimes = [files(~[files.isdir]).datenum];
% % % % % % %  Sort based on time modified
% % % % % % [~, sortedIndices] = sort(fileTimes);
% % % % % % sortedFileNames = fileNames(sortedIndices);

% Car_SteerAngle
for i = 1:length( Scenario_list)
   Scenario{i} = cmread(Scenario_list{i}); 
end
for i = 1:length( Scenario_list)
  % Plotting
  x = Scenario{1, i}.Time.data;
y1 = Scenario{1, i}.Car_SteerAngleFL.data;
y2 = Scenario{1, i}.Car_SteerAngleFR.data;

figure
plot(x,y1,x,y2)
title(['Scenario-', num2str(i), ' Car.SteerAngle FL & FR'])
legend('Car.SteerAngleFL','Car.SteerAngleFR')
xlabel('Time (s)');
ylabel('SteerAngle(rad)');
savefig(gcf,['C:\Users\ark8318\CM_Projects\SimOutput\ei702-15-16\20240404\2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i,'%03d'), '_Car_SteerAngleFL & FR']);

% filename = ['2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i), '_Car_SteerAngleFL & FR.png'];
%     exportgraphics(gcf, filename);
close all
end  
% 
% Car-Yaw & YawRate
for i = 1:length( Scenario_list)
  % Plotting
  x = Scenario{1, i}.Time.data;
y1 = Scenario{1, i}.Car_Yaw.data;
y2 = Scenario{1, i}.Car_YawRate.data;

figure
yyaxis('left')
plot(x,y1)
ylabel('YawAngle(rad)');
yyaxis('right')
plot(x,y2)
title(['Scenario-', num2str(i), ' Car.Yaw & YawRate'])
legend('Car.Yaw','Car.YawRate')
xlabel('Time (s)');
ylabel('YawRate(rad/s)');
savefig(gcf,['C:\Users\ark8318\CM_Projects\SimOutput\ei702-15-16\20240404\2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i,'%03d'), '_Car_Yaw']);

% filename = ['2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i), '_Car_Yaw & YawRate.png'];
%     exportgraphics(gcf, filename);
close all
end  
% 
% % % % % Car-YawRate
% % % % for i = 1:length( Scenario_list)
% % % %   % Plotting
% % % %   x = Scenario{1, i}.Time.data;
% % % % y1 = Scenario{1, i}.Car_YawRate.data;
% % % % 
% % % % figure
% % % % plot(x,y1)
% % % % title(['Scenario-', num2str(i), ' Car-YawRate'])
% % % % legend('Car-YawRate')
% % % % xlabel('Time (s)');
% % % % ylabel('YawRate(rad/s)');
% % % % savefig(gcf,['C:\Users\ark8318\CM_Projects\SimOutput\ei702-15-16\20240404\2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i,'%03d'), '_Car_YawRate']);
% % % % 
% % % % % filename = ['2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i), '_Car_Yaw & YawRate.png'];
% % % % %     exportgraphics(gcf, filename);
% % % % close all
% % % % end  
% 
% 
 % Car-Acclerations {ax & ay}
for i = 1:length( Scenario_list)
  % Plotting
  x = Scenario{1, i}.Time.data;
y1 = Scenario{1, i}.Car_Gen_ax.data;
y2 = Scenario{1, i}.Car_Gen_ay.data;

figure
plot(x,y1,x,y2)
title(['Scenario-', num2str(i), ' Car.Acclerations {ax & ay}'])
legend('Car.ax','Car.ay')
xlabel('Time (s)');
ylabel('Acceleration(m/s^2)');
savefig(gcf,['C:\Users\ark8318\CM_Projects\SimOutput\ei702-15-16\20240404\2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_',num2str(i,'%03d'), '_Car_Acclerations']);

% filename = ['2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i), '_Car-Acclerations.png'];
%     exportgraphics(gcf, filename);
close all
end

% Car-Positions {tx & ty}
for i = 1:length( Scenario_list)
  % Plotting
  x = Scenario{1, i}.Time.data;
y1 = Scenario{1, i}.Car_Fr1_tx.data;
y2 = Scenario{1, i}.Car_Fr1_ty.data;

figure
plot(x,y1,x,y2)
title(['Scenario-', num2str(i), ' Car.Positions {tx & ty}'])
legend('Car.Fr1.tx','Car.Fr1.ty')
xlabel('Time (s)');
ylabel('Position(m)');
savefig(gcf,['C:\Users\ark8318\CM_Projects\SimOutput\ei702-15-16\20240404\2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i,'%03d'), '_Car_Positions']);

% filename = ['2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i), '_Car-Positions.png'];
%     exportgraphics(gcf, filename);
close all
end

% Car-Velocities {vx & vy}
for i = 1:length( Scenario_list)
  % Plotting
  x = Scenario{1, i}.Time.data;
y1 = Scenario{1, i}.Car_vx.data;
y2 = Scenario{1, i}.Car_vy.data;

figure
plot(x,y1,x,y2)
title(['Scenario-', num2str(i), ' Car.Velocities {vx & vy}'])
legend('Car.vx','Car.vy')
xlabel('Time (s)');
ylabel('Velocity(m/s)');
savefig(gcf,['C:\Users\ark8318\CM_Projects\SimOutput\ei702-15-16\20240404\2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i,'%03d'), '_Car_Velocities']);

% filename = ['2024-03-26-KICSAFe_Trajectory_Steer_Vel_Scenario_', num2str(i), '_Car-Velocities.png'];
%     exportgraphics(gcf, filename);
close all
end

    close all
