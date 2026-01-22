import pyautogui
from pathlib import Path

def get_checkbox_position(IMAGE_DIR):
    arquivo = Path(IMAGE_DIR) / "voto_clarice.png"
    PVx, PVy = pyautogui.locateCenterOnScreen(str(arquivo), confidence= 0.5)
    final_position = [PVx, PVy] # hardcoded due to software layout// hardcoded por causa do layout do software
    
    return final_position

def get_submit_position(IMAGE_DIR):
    arquivo = Path(IMAGE_DIR) / "submit.png"
    PSx, PSy = pyautogui.locateCenterOnScreen(str(arquivo), confidence= 0.8)
    final_position = [PSx, PSy] # hardcoded due to software layout// hardcoded por causa do layout do software
    
    return final_position