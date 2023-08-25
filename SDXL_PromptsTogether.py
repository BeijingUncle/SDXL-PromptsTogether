class SDXL_PromptsTogether:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bpg": ("STRING", {"default": "", "multiline": True}),
                "bpl": ("STRING", {"default": "", "multiline": True}),
                "bng": ("STRING", {"default": "", "multiline": True}),
                "bnl": ("STRING", {"default": "", "multiline": True}),
                "rp": ("STRING", {"default": "", "multiline": True}),
                "rn": ("STRING", {"default": "", "multiline": True}),
            }
        }
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("BASE Positive G", "BASE Positive L", "BASE Positive G+L", "BASE Negative G", "BASE Negative L", "REFINE Positive", "REFINE Negative")
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
