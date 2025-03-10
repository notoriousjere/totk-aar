import os
import struct
import sys
import ast
import subprocess

scaling_factor = float(sys.argv[1])
centered_HUD = ast.literal_eval(sys.argv[2])
blyt_folder = str(sys.argv[3])
shift_factor = (1 - scaling_factor) / scaling_factor
print("Centered HUD value is set to ", centered_HUD)
print("The scaling factor is ", scaling_factor)

def float_to_hex(f):
    """
    Converts float values into hex, strips the 0x prefix and prepends zeroes to
    always have length 8
    """
    return hex(struct.unpack('>I', struct.pack('<f', f))[0]).lstrip('0x').rjust(8,'0')

file_names = os.listdir(blyt_folder)
file_names.remove('AppMenuBG_00.bflyt')
print("Removing AppMenuBG_00.bflyt")
file_names.remove('AppMenuOverlay_00.bflyt')
print("Removing AppMenuOverlay_00.bflyt")
file_names.remove('PauseMenuBG_00.bflyt')
print("Removing PauseMenuBG_00.bflyt")
file_names.remove('ShopMenuParasailBG_00.bflyt')
print("Removing ShopMenuParasailBG_00.bflyt")
file_names.remove('ShortCutBG_00.bflyt')
print("Removing ShortCutBG_00.bflyt")
file_names.remove('TitleMenuBG_00.bflyt')
print("Removing TitleMenuBG_00.bflyt")
file_names.remove('PaMap_00.bflyt')
print("Removing PaMap_00.bflyt")
file_names.remove('EventFade_00.bflyt')
print("Removing EventFade_00.bflyt")
file_names.remove('EventFadeWipe_00.bflyt')
print("Removing EventFadeWipe_00.bflyt")
file_names.remove('AttentionLockOn_00.bflyt')
print("Removing AttentionLockOn_00.bflyt")
file_names.remove('EnemyInfo_00.bflyt')
print("Removing EnemyInfo_00.bflyt")
file_names.remove('BalloonMessage_00.bflyt')
print("Removing BalloonMessage_00.bflyt")
file_names.remove('AttentionBalloon_00.bflyt')
print("Removing AttentionBalloon_00.bflyt")

for name in file_names:
    file_loc = blyt_folder + "\\" + name
    
    with open(file_loc, 'rb') as f:
        content = f.read().hex()
            
    # Scale RootPane by scaling_factor
    x = float_to_hex(scaling_factor)
    source_str = '526F6F7450616E650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
    replace_str = '526F6F7450616E650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
    content = content.replace(source_str.lower(), replace_str.lower())
    
    # Scale BG_00 by inverse scaling_factor
    x = float_to_hex(1/scaling_factor)
    source_str = '42475F3030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
    replace_str = '42475F3030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
    content = content.replace(source_str.lower(), replace_str.lower()) 
    
    # Scale BG_00 by inverse scaling_factor
    x = float_to_hex(1/scaling_factor)
    source_str = '42475F3030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
    replace_str = '42475F3030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
    content = content.replace(source_str.lower(), replace_str.lower())
    
    
    if  name == 'LoadingFade_00.bflyt':
        # Scale N_Base
        x = float_to_hex(1/scaling_factor)
        source_str = '4E5F426173655F303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
        replace_str = '4E5F426173655F303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Shift N_Logo
        x = float_to_hex(-70)
        source_str = '4E5F4C6F676F5F303000000000000000000000000000000000000000000000000000000000000000'
        replace_str = '4E5F4C6F676F5F3030000000000000000000000000000000000000000000000000000000' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # # Shift N_Tips
        # x = float_to_hex(-400)
        # source_str = '4E5F546970735F303000000000000000000000000000000000000000000000000000000000000000'
        # replace_str = '4E5F546970735F3030000000000000000000000000000000000000000000000000000000' + x
        # content = content.replace(source_str.lower(), replace_str.lower())
        
        # Shift N_Status
        x = float_to_hex(70)
        source_str = '4E5F5374617475735F30300000000000000000000000000000000000000000000000000000000000'
        replace_str = '4E5F5374617475735F303000000000000000000000000000000000000000000000000000' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
 
    if name == 'PauseMenuOverlay_00.bflyt':
        # Scale P_FooterBase
        x = float_to_hex(1/scaling_factor)
        source_str = '505F466F6F746572426173655F303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
        replace_str = '505F466F6F746572426173655F303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Scale S_DecoScissor
        x = float_to_hex(1/scaling_factor)
        source_str = '535F4465636F53636973736F725F303000000000000000000000000000000000000000000000F841000000000000000000000000000000000000803F0000803F'
        replace_str = '535F4465636F53636973736F725F303000000000000000000000000000000000000000000000F841000000000000000000000000000000000000803F' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Shift P_FooterBase
        x = float_to_hex(-66)
        source_str = '505F466F6F746572426173655F303000000000000000000000000000000000000000000000000000'
        replace_str = '505F466F6F746572426173655F3030000000000000000000000000000000000000000000' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Shift S_DecoScissor
        x = float_to_hex(-28)
        source_str = '535F4465636F53636973736F725F303000000000000000000000000000000000000000000000F841'
        replace_str = '535F4465636F53636973736F725F30300000000000000000000000000000000000000000' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Shift Pa_GuideL
        x = float_to_hex(-25)
        source_str = '50615F47756964654C5F30300000000000000000000000000000000000000000008046C400000C42'
        replace_str = '50615F47756964654C5F30300000000000000000000000000000000000000000008046C4' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Shift A_Align
        x = float_to_hex(-25)
        source_str = '415F416C69676E5F3030000000000000000000000000000000000000000000000000024300000C42'
        replace_str = '415F416C69676E5F30300000000000000000000000000000000000000000000000000243' + x
        content = content.replace(source_str.lower(), replace_str.lower())
       
        
    if name == 'CameraPointer_00.bflyt':
        # Scale N_InOutScop
        x = float_to_hex(1/scaling_factor)
        source_str = '4E5F496E4F757453636F70655F303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
        replace_str = '4E5F496E4F757453636F70655F303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Scale W_shadow_01
        x = float_to_hex(1/scaling_factor)
        source_str = '575F536861646F775F30310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
        replace_str = '575F536861646F775F30310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        
    if name == 'AppMap_00.bflyt':
        # Scale N_BlurInOut_00
        x = float_to_hex(1/scaling_factor)
        source_str = '4E5F426C7572496E4F75745F30300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
        replace_str = '4E5F426C7572496E4F75745F30300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Scale N_BlurInOut_01
        x = float_to_hex(1/scaling_factor)
        source_str = '4E5F426C7572496E4F75745F30310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
        replace_str = '4E5F426C7572496E4F75745F30310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Scale N_BlurInOut_02
        x = float_to_hex(1/scaling_factor)
        source_str = '4E5F426C7572496E4F75745F30320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
        replace_str = '4E5F426C7572496E4F75745F30320000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Scale N_BlurInOut_03
        x = float_to_hex(1/scaling_factor)
        source_str = '4E5F426C7572496E4F75745F30330000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F0000803F'
        replace_str = '4E5F426C7572496E4F75745F30330000000000000000000000000000000000000000000000000000000000000000000000000000000000000000803F' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
    
    if name == 'EnvironmentInfo_00.bflyt':
        # Shift RootPane
        x = float_to_hex(-20)
        source_str = '526F6F7450616E650000000000000000000000000000000000000000000000000000000000000000'
        replace_str = '526F6F7450616E6500000000000000000000000000000000000000000000000000000000' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        
    if name == 'PlayerStatus_00.bflyt':
        # Shift RootPane
        x = float_to_hex(50)
        source_str = '526F6F7450616E650000000000000000000000000000000000000000000000000000000000000000'
        replace_str = '526F6F7450616E6500000000000000000000000000000000000000000000000000000000' + x
        content = content.replace(source_str.lower(), replace_str.lower())
            
        
    # if name == 'PlayerStatus3D_00.bflyt':
    #     # Shift N_ExtraStaminaTarget_01
    #     x = float_to_hex(400)
    #     source_str = '45787472615374616D696E615461726765745F303100000000000000000000403AC400009843'
    #     replace_str = '45787472615374616D696E615461726765745F303100000000000000000000403AC4' + x
    #     content = content.replace(source_str.lower(), replace_str.lower())
           
    
    if name == 'AppMap_00.bflyt':        
        # Shift RootPane
        x = float_to_hex(-20)
        source_str = '526F6F7450616E650000000000000000000000000000000000000000000000000000000000000000'
        replace_str = '526F6F7450616E6500000000000000000000000000000000000000000000000000000000' + x
        content = content.replace(source_str.lower(), replace_str.lower())
        
        # Shift N_MiniMap
        x = float_to_hex(20) 
        source_str = '4E5F4D696E694D61705F303000000000000000000000000000000000000000000000000000000000'
        replace_str = '4E5F4D696E694D61705F3030000000000000000000000000000000000000000000000000' + x
        content = content.replace(source_str.lower(), replace_str.lower())
            
    
    with open(file_loc, 'wb') as f:
        f.write(bytes.fromhex(content))
        
 