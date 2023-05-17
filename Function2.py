def vac_feedback(vac, efficacy):
    print(f"{vac} Vaccines is having {efficacy}% efficacy")
    if (efficacy > 50 ) and (efficacy <= 75):
        print("Seems not so effective, Needs  more trial")
    elif (efficacy > 75 ) and (efficacy < 90):
        print("Can consider this vaccine")
    elif efficacy >= 90:
        print("Sure, will take the shot")
    else:
        print("needs many more trials")
#
# vac_feedback("Pfizer", 95)
# vac_feedback("unknown", 45)
vac_feedback(efficacy= 20, vac="Pfizer")