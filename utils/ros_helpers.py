import sys
if '/duckietown/simulation' not in sys.path:
    sys.path.append('/duckietown/simulation')

def launch_env(simclass=None):
    print(sys.path)
    from src.gym_duckietown.simulator import Simulator

    simclass = Simulator if simclass is None else simclass

    env = simclass(
        seed=123, # random seed
        map_name="loop_empty",
        max_steps=500001, # we don't want the gym to reset itself
        domain_rand=0,
        camera_width=640,
        camera_height=480,
        accept_start_angle_deg=4, # start close to straight
        full_transparency=True,
        distortion=True,
    )
    return env