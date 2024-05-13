import maya.cmds as cmds
import os

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

#this function is used to check the frame number of the video
def check_frame_number(sequence_path):
    try:
        with open(sequence_path, "r") as file:
            for line in line:
                if line
    except:
        print("error reading the file")
        raise
    return None

# Example usage
export_dir = "F:\\Jerry\\Test_Jackson_Automation"#this is the destination file
frame_start = 1#start frame
frame_end = 270#end frame

export_obj_sequence(export_dir, frame_start, frame_end)