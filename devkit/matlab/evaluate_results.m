clear all; close all; dbstop error;

resultDir = 'results/'

model = 'pretrained-sceneflow'
resultFolder = strcat(resultDir, model, '/');
dataFolder = 'data_scene_flow/custom-testing/';

% error threshold
tau = [3 0.05];

for index = 1:5
    i = index - 1
    
    dispmapPath = strcat(resultFolder, '00000', int2str(i), '_10.png');
    D_est = disp_read(dispmapPath);

    groundTruthPath = strcat(dataFolder, 'disp_occ_0/00000', int2str(i), '_10.png');
    D_gt = disp_read(groundTruthPath);

    coloredDispmapPath = strcat(resultFolder, '00000', int2str(i), '_10_disp_colored.png');
    imwrite(disp_to_color(D_est), coloredDispmapPath);

    errorMapPath = strcat(resultFolder, '00000', int2str(i), '_10_disp_error.png')
    
    d_err = disp_error(D_gt,D_est,tau);
    D_err = disp_error_image(D_gt,D_est,tau);

    imwrite(D_err, errorMapPath)
    sprintf('Disparity Error for 00000%d_10.png: %.2f %%', i, d_err*100)
end
