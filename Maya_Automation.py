import maya.cmds as cmds
import os
import json

#define a function to accept the info file and return the frame numbers value
def get_frame_numbers(json_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)
    
    frames = data.get("frames")#get the frames key
    if frames is None:
        raise ValueError("No frames key found in the file")
    return frames
    
json_file_path = "E:\\ARFriendInteract\\Captures\\iPhone2\\20240422_010Jackson_81\\take.json"
frame_numbers = get_frame_numbers(json_file_path)#frame number

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


# Example usage
export_dir = "F:\\Jerry\\Automate_Maya_OBJ"#this is the destination file
frame_start = 1#start frame
frame_end = frame_numbers#end frame

export_obj_sequence(export_dir, frame_start, frame_end)
