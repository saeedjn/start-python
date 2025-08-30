def show_info(**info):
    for key, value in info.items():
        print(f"{key} : {value}")

show_info(name="Ali", age=25, city= "tehran")