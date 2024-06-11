import py_avataaars as pa

class avatar:

    def create_avatar(self):
        print("Customize your avatar:")
        skin_color = input("Enter skin color (e.g., LIGHT, BROWN, TANNED): ")
        hair_color = input("Enter hair color (e.g., AUBURN, BLACK, BLONDE): ")

        # Add more input prompts for other avatar features (eyes, mouth, etc.)

        avatar = pa.PyAvataaar(
            style=pa.AvatarStyle.CIRCLE,
            skin_color=pa.SkinColor[skin_color],
            hair_color=pa.HairColor[hair_color],
            # Add other parameters here
        )

        def display_avatar():
            avatar.render_png_file("my_avatar.png")
            
if __name__ == "__main__":
    av = avatar
    av.create_avatar()