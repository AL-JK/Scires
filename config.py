class Config:
    def __init__(self, env):
        self.device = "cpu"

        self.env = env
        self.obs_shape = env.observation_space.shape
        self.act_shape = env.action_space.shape
        self.num_options = 5

        self.lr = 1e-3
        self.temperature = 1.0