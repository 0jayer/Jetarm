import mujoco
import mujoco.viewer
import numpy as np
import time
# from mujoco.glfw import glfw
import glfw

def main() -> None:
    global temp_step,x_mov,y_mov,z_mov,x_neg,y_neg,z_neg
    temp_step=0
    assert mujoco.__version__ >= "3.1.0", "Please upgrade to mujoco 3.1.0 or later."

    # Load the model and data.
    model = mujoco.MjModel.from_xml_path("Jetarm/scene.xml")
    data = mujoco.MjData(model)
    

    with mujoco.viewer.launch_passive(
        model=model,
        data=data,
        show_left_ui=False,
        show_right_ui=False,
        
    ) as viewer:
         
         mujoco.mj_resetData(model, data)
         viewer.sync()

        # Simulation/rendering loop
         while viewer.is_running():
    
            mujoco.mj_step(model, data)
            viewer.sync()



if __name__ == "__main__":
    main()