from init import logs, user_me, bot
def pre_init():
    import os
    anti_channel_file = "./data/anti_channel.pkl"
    if os.path.exists(anti_channel_file):
        return True
    else:
        os.mkdir("./data")
        with open("./data/anti_channel.pkl","w") as pkl_file:
            pass
if __name__ == "__main__":
    pre_init()
    logs.info(f"@{user_me.username} 运行成功！")
    bot.run()
