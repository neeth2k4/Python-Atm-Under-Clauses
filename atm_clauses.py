import math
print("Admin side")
#a,b,c are respective available 100,200,500 notes in atm
a,b,c=0000,5000,2500
amount=int(input("Enter the money you would like to withdraw(multiples of 100)"))
if amount%100 !=0:
    print("Enter 100 multiples only")

elif a>5000 and b>2500 and c>1000:
    numa=(0.33)*amount
    print("Amount partitioned for 100 notes:",numa)
    x=math.ceil(numa/100)
    print("x:",x)

    numb=(0.33)*amount
    print("Amount partitioned for 200 notes:",numb)
    y=math.floor(numb/200)
    print("y:",y)

    numc=(0.33)*amount
    print("Amount partitioned for 500 notes:",numc)
    z=math.floor(numc/500)
    print("z:",z)

    if((x*100)+(y*200)+(z*500)!=amount):
        v=amount-((x*100)+(y*200)+(z*500))
        if (v)%500==0:
            p=int(v/500)
            z=z+p
        elif (v)%200==0:
            p=int(v/200)
            y=y+p
        elif (v)%100==0:
            p=int(v/100)
            x=x+p
        a=a-x #for 100 notes
        b=b-y #for 200 notes
        c=c-z  #for 500 notes
        print("Comparison:",(x*100)+(y*200)+(z*500))
        print("number of '100' notes withdrew(1):",x)
        print("number of notes remaining",a)
        print("number of '200' notes withdrew:",y)
        print("number of notes:",b)
        print("number of '500' notes withdrew:",z)
        print("number of notes:",c)
    else:
        a=a-x #for 100 notes
        b=b-y #for 200 notes
        c=c-z  #for 500 notes
        print("Comparison:",(x*100)+(y*200)+(z*500))
        print("number of '100' notes withdrew(2):",x)
        print("number of notes remaining",a)
        print("number of '200' notes withdrew:",y)
        print("number of notes:",b)
        print("number of '500' notes withdrew:",z)
        print("number of notes:",c)

else:
    if a!=0:
        numa=int((0.50)*amount)
        w=math.ceil(numa/100)

        numb=int((0.50)*amount)
        x=math.floor(numb/200)

        if((w*100)+(x*200))!= amount:
            v=amount-((w*100)+(x*200))
            print("a",v)
            if (v)%100==0:
                p=int(v/100)
                w=w+p
            if (v)%200==0:
                p=int(v/200)
                x=x+p
            print("comp",(w*100)+(x*200))
            a=a-w #for 100 notes
            b=b-x #for 200 notes
            print("number of '100' notes withdrew:",w)
            print("number of notes remaining",a)
            print("number of '200' notes withdrew:",x)
            print("number of notes(2a):",b)
        else:
            a=a-w #for 100 notes
            b=b-x #for 200 notes
            print("number of '100' notes withdrew:",w)
            print("number of notes remaining",a)
            print("number of '200' notes withdrew:",x)
            print("number of notes(2):",b)
    else:
        if amount == 100 or amount ==300:
            print("Enter a multiple of 200 or 500")
        else:
            numb=(0.50)*amount
            w=math.floor(numb/200)

            numc=(0.50)*amount
            x=math.floor(numc/500)

            if((w*200)+(x*500))!= amount:
                v=amount-((w*200)+(x*500))
                if v==100:
                    x=x+1
                    w=w-2
                elif (v)%500==0:
                    p=int(v/500)
                    x=x+p
                elif (v)%200==0:
                    p=int(v/200)
                    w=w+p
                elif v==300:
                    x=x+1
                    w=w-1
                b=b-w #for 200 notes
                c=c-x #for 500 notes
                print("comp:",(w*200)+(x*500))
                print("number of '200' notes withdrew:",w)
                print("number of notes:",b)
                print("number of '500' notes withdrew:",x)
                print("number of notes(3):",c)
            else:
                b=b-w #for 200 notes
                c=c-x #for 500 notes
                print("compi:",(w*200)+(x*500))
                print("number of '200' notes withdrew:",w)
                print("number of notes:",b)
                print("number of '500' notes withdrew:",x)
                print("number of notes(3):",c)
