# Automation Pipeline For Maya  
Python script can fully automate the procedure of importing animation sequences into Maya and then exporting OBJ files into the selected directory  

# Python Script Explanation  
process_multiple_animation_sequences() is the main function, it will open a folder that contains many sequence json files that need to be processed. Then, it goes through each json file one by one, call the function mgApplyFaceMocap() to process the animation sequence and apply the animation to face rig. get_frame_numbers() will get the frame number of that sequence, then it pass the arguements to function export_obj_sequence(), this step will export OBJ mesh to the destination folder.
# OBJ Mesh Example
eg:  
<img width="478" alt="image" src="https://github.com/JerryTseee/Maya_Auto_Export_OBJ/assets/126223772/49130552-05fd-41c2-b379-d6d39de9e08a">  
<img width="530" alt="image" src="https://github.com/JerryTseee/Maya_Auto_Export_OBJ/assets/126223772/8e7c79c5-7720-4d7f-80db-439236f0ae18">
