for amount_loaded in range(0, 105, 5):
    if amount_loaded == 25:
        print(amount_loaded, "\n1/4 the way there")
    elif amount_loaded == 50:
        print(amount_loaded, "\n1/2 the way there")
    elif amount_loaded == 75:
        print(amount_loaded, "\n3/4 the way there")
    elif amount_loaded == 100:
        print(amount_loaded, "\nLoading complete!")
    else:
        print(amount_loaded)
