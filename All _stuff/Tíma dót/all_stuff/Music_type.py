#definition for music_func goes here
def music_func(music_type = "Classical Rock", music_group = "The Beatles", singer = "Freddie Mercury"):
    print("The best kind of music is", music_type)
    print("The best music group is", music_group)
    print("The best singer is", singer)



def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()