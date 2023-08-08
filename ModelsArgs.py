def get_upscale_model_args(model_index):
    upscale_models_args = {
        # Arguments for upscaling model ESPCN
        1: {'model_path': "Models/ESPCN/ESPCN_x4.pb",  # end of file name must be same as ratio arg
            'model_index': "espcn",
            'ratio': 4},  # 2 or 3 or 4

        # Arguments for upscaling model EDSR
        2: {'model_path': "Models/EDSR/EDSR_x4.pb",  # end of file name must be same as ratio arg
            'model_index': "edsr",
            'ratio': 4},  # 2 or 3 or 4

        # Arguments for upscaling model LapSRN
        3: {'model_path': "Models/LapSRN/LapSRN_x4.pb",  # end of file name must be same as ratio arg
            'model_index': "lapsrn",
            'ratio': 4}  # 2 or 4 or 8
    }
    return upscale_models_args[model_index]
