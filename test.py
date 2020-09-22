import gym
import pybullet_envs #import gym and then pybullet_envs

#some needs mpi4py and mpi environment
#https://stackoverflow.com/questions/14004457/error-loading-mpi-dll-in-mpi4py ERIC's answer
#can't find how to change render's default view angle

#some has to define render from the beginning to render
#env = gym.make("MinitaurBulletEnv-v0", render=True)
#env = gym.make("HumanoidDeepMimicBackflipBulletEnv-v1", renders=True)#need mpi
#env = gym.make("HumanoidDeepMimicWalkBulletEnv-v1", renders=True)#need mpi
#env = gym.make("CartPoleContinuousBulletEnv-v0", renders=True)
#env = gym.make("RacecarBulletEnv-v0", renders=True)
#env = gym.make("RacecarZedBulletEnv-v0", renders=True)
#env = gym.make("KukaBulletEnv-v0", renders=True)
#env = gym.make("KukaCamBulletEnv-v0", renders=True)
#env = gym.make("AntBulletEnv-v0", render=True)
#env = gym.make("HalfCheetahBulletEnv-v0", render=True)
#env = gym.make("HumanoidBulletEnv-v0", render=True)
#env = gym.make("HopperBulletEnv-v0", render=True)
#env = gym.make("Walker2DBulletEnv-v0", render=True)
#env = gym.make("InvertedPendulumBulletEnv-v0")
env = gym.make("InvertedDoublePendulumBulletEnv-v0")
#env = gym.make("InvertedPendulumSwingupBulletEnv-v0")
#env = gym.make("InvertedDoublePendulumSwingupBulletEnv-v0")

env.render()#pybullet envs define render outside the loop
env.reset()#state and reward, done -> identical to gym
while True:

    action = env.action_space.sample() # your agent here (this takes random actions)
    observation, reward, done, info = env.step(action)
    print(observation, reward, done, info)
    if done:
        observation = env.reset()
