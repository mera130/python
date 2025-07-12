def no_note(a):
    Q=[1000,500,200,100,50,20,10]
    x=0
    for i in range(7):
        q= Q[i]
        x = a//e
        print("note of {} = {}".format (q,x))
        a = a%q

value = int(input("give the sum"))
no_notes(value)
    