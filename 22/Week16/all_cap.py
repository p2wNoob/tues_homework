def all_cap(words):
    caps = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    result = True
    for char in words:
        if char not in caps:
            result = False
            break
    print(result)

all_cap("gosho")
all_cap("romanreignsisagoodwrestler")
all_cap("ROMANREIGNSSUCKS")
all_cap("KEVINDUNNHASTHEWHITESTTEETHINWWe")
all_cap("APOLLOCREWSTEETHAREWHITHERTHANKEVINDUNNS")
