from gym.envs.registration import register

register(
    id='CartPoleContinuous-v0',
    entry_point='CartPoleContinuous.envs:CartPoleEnv',  # Replace 'custom_env' with the name of your file
)