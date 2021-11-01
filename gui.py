import dearpygui.dearpygui as dpg

pets = {
    'none': 'assets/pets/png/none.png',
    'bear': 'assets/pets/png/bear.png',
    'buffalo': 'assets/pets/png/buffalo.png',
    'bunny' : 'assets/pets/png/bunny.png',
    'cat' : 'assets/pets/png/cat.png',
    'cow' : 'assets/pets/png/cow.png',
    'deer' : 'assets/pets/png/deer.png',
    'dog' : 'assets/pets/png/dog.png',
    'elephant' : 'assets/pets/png/elephant.png',
    'fox' : 'assets/pets/png/fox.png',
    'giraffe' : 'assets/pets/png/giraffe.png',
    'goat' : 'assets/pets/png/goat.png',
    'gorilla' : 'assets/pets/png/gorilla.png',
    'hawk' : 'assets/pets/png/hawk.png',
    'hippo' : 'assets/pets/png/hippo.png',
    'horse' : 'assets/pets/png/horse.png',
    'koala' : 'assets/pets/png/koala.png',
    'leo' : 'assets/pets/png/leo.png',
    'monkey' : 'assets/pets/png/monkey.png',
    'panda' : 'assets/pets/png/panda.png',
    'pig' : 'assets/pets/png/pig.png',
    'rino' : 'assets/pets/png/rino.png',
    'snake' : 'assets/pets/png/snake.png',
    'tiger' : 'assets/pets/png/tiger.png',
    'walrus' : 'assets/pets/png/walrus.png',
    'wolf' : 'assets/pets/png/wolf.png',
}

all_pets = list(pets.keys())

dpg.create_context()

#Load Pets Textures
with dpg.texture_registry(show=True):
    for pet in all_pets:
        width, height, channels, data = dpg.load_image(pets[pet])
        dpg.add_static_texture(width, height, data, tag=pet)

with dpg.window(label="RNG TTT"):
    with dpg.group(horizontal=True):
        dpg.add_image_button("none", tag='board_00')
        dpg.add_image_button("none", tag='board_01')
        dpg.add_image_button("none", tag='board_02')
    
    with dpg.group(horizontal=True):
        dpg.add_image_button("none", tag='board_10')
        dpg.add_image_button("none", tag='board_11')
        dpg.add_image_button("none", tag='board_12')

    with dpg.group(horizontal=True):
        dpg.add_image_button("none", tag='board_20')
        dpg.add_image_button("none", tag='board_21')
        dpg.add_image_button("none", tag='board_22')

    dpg.add_text("Your hand:")
    with dpg.group(horizontal=True):
        dpg.add_image_button("none", tag='hand_00')
        dpg.add_image_button("none", tag='hand_01')
        dpg.add_image_button("none", tag='hand_02')

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()