# import torch
# from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

# class Model:
    
#     def __init__(self) -> None:
#         model_id = "stabilityai/stable-diffusion-2-1"
#         pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
#         pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
#         self.model = pipe.to('cuda')
    
#     def train(self) -> None:
        
#         ...
