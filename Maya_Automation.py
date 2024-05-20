import os
import sys
import imp
import json
import maya.cmds as cmds



#define the function to import the animation sequence from the selected json file
def mgApplyFaceMocap(filePath):
    objLs = cmds.ls(sl=1)
    namespace = ''
        
    if len(objLs)>0:
        if ':' in objLs[0]:
            namespace = objLs[0].split(':')[0] + ':'
        else:
            namespace = ''
    anim_keys_file = imp.load_source('', filePath)
    
    anim_keys = anim_keys_file.anim_keys_dict
    
    for dict_key in anim_keys:
        keyframes_list = anim_keys[dict_key]
        ctrl = dict_key
        attr = 'translateY'
        if '.' in ctrl:
            ctrl_string_list = ctrl.split('.')
            ctrl = ctrl_string_list[0]
            if len(ctrl_string_list)>2:
                attr = ctrl_string_list[1].replace('Location', 'translate').replace('Rotation', 'rotate').replace('Scale', 'scale') + ctrl_string_list[-1].upper()
            else:
                attr = 'translate' + ctrl_string_list[-1].upper()

        # check for numbers at the end of cntrl name
        
        ctrl_name = ctrl
        if ctrl_name.split('_')[-1].isdigit():
            ctrl_name = ctrl_name.replace('_' + ctrl_name.split('_')[-1], '')
        ctrl_name = namespace + ctrl_name

        if cmds.objExists(ctrl_name):
            for key_num in range(0,len(keyframes_list)):
                key_val = keyframes_list[key_num]
                cmds.setKeyframe(ctrl_name, attribute=attr, v = key_val[0], t=key_val[1] )
        else:
            print('Skipping ' + ctrl_name + ' as no such object exists.')
            
    print('Applied Animation to Face Rig.')



#define a function to get the frame value of the selected video
def get_frame_numbers(json_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)
    
    frames = data.get("frames")#get the frames key
    if frames is None:
        raise ValueError("No frames key found in the file")
    return frames



#define a function to export the OBJ files into the destination
def export_obj_sequence(export_dir, frame_start, frame_end):
    selection = cmds.ls(selection=True)

    if not selection:
        #end of the export
        print("Nothing selected, nothing to export")
        return

    if not os.path.isdir(export_dir):
        #if no such destination file, then end
        print("Specified directory doesn't exist:", export_dir)
        return

    #start to export
    for i in range(frame_start, frame_end + 1):
        try:
            cmds.currentTime(i, edit=True)
        except:
            print("Couldn't go to frame", i)
            raise

        # Generate the filename based on the frame number
        filename = os.path.join(export_dir, 'Object_{:03d}.obj'.format(i))

        try:
            cmds.file(filename, save=False, force=True, exportSelected=True, type="OBJexport")
        except:
            print("Couldn't save file:", filename)
            raise

        print("Exported:", filename)



#define the main function
def main():
    
    #import animation seqeunce
    filePath = "C:\\Users\\Yinghao\\Documents\\iPhone2MHseq\\pipeline\\Unreal\\NewLevelSequence4_cooper_face_anim.json"
    if not os.path.isfile(filePath):
        print("Error: Invalid file")
        return
    mgApplyFaceMocap(filePath)
    print("successfully load into the animation sequence")

    #from json file get frame value
    json_file_path = "E:\\ARFriendInteract\\Captures\\iPhone2\\20240422_010Jackson_81\\take.json"
    if not os.path.isfile(json_file_path):
        print("Error: Invalid file")
        return
    frame_numbers = get_frame_numbers(json_file_path)
    print("successfully get the frame value")

    #start to export the OBJ files
    export_dir = "F:\\Jerry\\Automate_Maya_OBJ"#selected destination folder
    if not os.path.isdir(export_dir):
        print("Error: Invalid directory")
        return
    frame_start = 1
    frame_end = frame_numbers
    export_obj_sequence(export_dir, frame_start, frame_end)
    print("successfully export the OBJ files")

    return



#call the main function
main()