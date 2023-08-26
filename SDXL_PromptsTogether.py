class SDXL_PromptsTogether:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bpg": ("STRING", {"default": "", "display": "CLIP G / BASE Positive", "multiline": True}),
                "bpl": ("STRING", {"default": "CLIP L / BASE Positive", "multiline": True}),
                "bng": ("STRING", {"default": "CLIP G / BASE Negative", "multiline": True}),
                "bnl": ("STRING", {"default": "CLIP L / BASE Negative", "multiline": True}),
                "rp": ("STRING", {"default": "REFINER Positive", "multiline": True}),
                "rn": ("STRING", {"default": "REFINER Negative", "multiline": True}),
            }
        }
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("CLIP G / BASE P", "CLIP L / BASE P", "CLIP G+L / BASE P", "CLIP G / BASE N", "CLIP L / BASE N", "REFINER P", "REFINER N")
    FUNCTION = "prompts"

    CATEGORY = "utils"

    def prompts(self, bpg, bpl, bng, bnl, rp, rn):
        return(bpg, bpl, bpg + ' , ' + bpl, bng, bnl, rp, rn)


NODE_CLASS_MAPPINGS = {
    "SDXL_PromptsTogether": SDXL_PromptsTogether
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXL_PromptsTogether": "SDXL Prompts Together",
}
