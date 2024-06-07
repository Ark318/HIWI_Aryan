% folder path
Scenario_list_path = pwd;

% list
files = dir(Scenario_list_path);

% filenames (excluding folders)
fileNames = {files(~[files.isdir]).name};

% time list
startValue = 0.04;
increment = 0.02;
endValue = 5.00;

% Generate the list
time = (startValue:increment:endValue)';

% Initialize 
velFiles = {};
posFiles = {};
accelFiles = {};

% Filter files with '.txt' extension and sort into respective lists
for i = 1:length(fileNames)
    if endsWith(fileNames{i}, '.txt')
        fullFileName = fullfile(Scenario_list_path, fileNames{i});
        
        if contains(fileNames{i}, 'Test_vel')
            velFiles{end+1} = fullFileName;
        elseif contains(fileNames{i}, 'Test_pos')
            posFiles{end+1} = fullFileName;
        elseif contains(fileNames{i}, 'Test_accel')
            accelFiles{end+1} = fullFileName;
        end
    end
end

velX = cell(length(velFiles),1);
velY = cell(length(velFiles),1);
for j = 1:length(velFiles)
    velTable = readcell(velFiles{j});
    velTable = velTable(3:end,:);
    velTable = cell2table(velTable(2:end,:), "VariableNames", [velTable(1,:)]);
    velX{j} = velTable.X;
    velY{j} = velTable.Y;
    % Plotting
x = time;
y1 = velX{j};
y2 = velY{j};

figure
plot(x,y1,x,y2)
title(['Scenario-', num2str(j), ' Car-Velocities {vx & vy}'])
legend('Car-vx','Car-vy')
xlabel('Time (s)');
ylabel('Velocity(m/s)');
savefig(gcf,['C:\Users\aryan\OneDrive\Documents\IAE\HIWI\logs latest\Carla_Scenario_', num2str(j,'%03d'), '_Car_Velocities']);

% close all
   
end

accelX = cell(length(accelFiles),1);
accelY = cell(length(accelFiles),1);
for j = 1:length(accelFiles)
    accelTable = readcell(accelFiles{j});
    accelTable = accelTable(3:end,:);
    accelTable = cell2table(accelTable(2:end,:), "VariableNames", [accelTable(1,:)]);
    accelX{j} = accelTable.X;
    accelY{j} = accelTable.Y;
    accelTime = accelTable.Time;
    % Plotting
x = accelTime;
y1 = accelX{j};
y2 = accelY{j};

figure
plot(x,y1,x,y2)
title(['Scenario-', num2str(j), ' Car-Acclerations {ax & ay}'])
legend('Car-ax','Car-ay')
xlabel('Time (s)');
ylabel('Acceleration(m/s^2)');
savefig(gcf,['C:\Users\aryan\OneDrive\Documents\IAE\HIWI\logs latest\Carla_Scenario_', num2str(j,'%03d'), '_Car_Acclerations']);

% close all
   
end

posX = cell(length(posFiles),1);
posY = cell(length(posFiles),1);
for j = 1:length(posFiles)
    posTable = readcell(posFiles{j});
    posTable = posTable(3:end,:);
    posTable = cell2table(posTable(2:end,:), "VariableNames", [posTable(1,:)]);
    posX{j} = posTable.X;
    posY{j} = posTable.Y;
    % Plotting
x = time;
y1 = posX{j};
y2 = posY{j};

figure
plot(x,y1,x,y2)
title(['Scenario-', num2str(j), ' Car-Positions {px & py}'])
legend('Car-px','Car-py')
xlabel('Time (s)');
ylabel('Position(m)');
savefig(gcf,['C:\Users\aryan\OneDrive\Documents\IAE\HIWI\logs latest\Carla_Scenario_', num2str(j,'%03d'), '_Car_Positions']);

% close all
   
end

