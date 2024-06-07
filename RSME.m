x = Scenario{1, 1}.Time.data;
y_1 = Scenario{1, 1}.Car_Yaw.data;
y_2 = Scenario{1, 2}.Car_Yaw.data; 

%MAE
mae = mean(abs(y_1-y_2));
fprintf('Mean Absolute Error (MAE): %.4f\n', mae);

% RMSE
rmse = sqrt(mean((y_1 - y_2).^2));
fprintf('Root Mean Square Error (RMSE): %.4f\n', rmse);

% Plot actual and predicted data
plot(x, y_1, 'b-', x, y_2, 'r--');
xlabel('a');
ylabel('b');
title('vs. Data');
legend('', '');
grid on;
% hold on;

% Calculate error
error = y_1 - y_2;

% Plot error
plot(x, error, 'g-');
xlabel('');
ylabel('Error');
title('Error Plot');
grid on;