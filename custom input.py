def custom_input(input_type="str", input_msg="", error_msg=""):
    while True:
        i = input(f"{input_msg}")
        
        try:
            if input_type == "str":
                return str(i)

            elif input_type == "int":
                return int(i)

            elif input_type == "float":
                i = i.replace(",", ".", 1)
                return float(i)

        except:
            print(error_msg + "\n")
