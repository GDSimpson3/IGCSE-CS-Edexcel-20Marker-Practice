participantData = [
    # ["Name",age,swim,cycle,run, TotalTime]
]

MaxParticipants = 50
MinAge = 16

count = 0

FastestParticipant = ["NAME",19,0,0,0,0] #Total time wise - ["Name",age,swim,cycle,run, TotalTime] hence check via Fastest[5]

TotalTimes = []

while count < MaxParticipants:
    count = count + 1
    Participant = []
    try: 
        name = str(input(f"Please enter the Participants Name (type DONE to exit): "))

        if name.upper() == 'DONE':
            if input("Are you sure you want to Quit? (y/n): ").upper() == 'Y':
                break

        Participant.append(name)
        age = int(input("Please enter the Participant's Age: "))

        if age >= MinAge:
            # print("Participant Too young")
        
            Participant.append(age)
            Swim = int(input(f"Please Enter {name}'s Score for their Swimming: "))
            Cycle = int(input(f"Please Enter {name}'s Score for their Cycling: "))
            Running = int(input(f"Please Enter {name}'s Score for their Running: "))

            Participant.append(Swim)
            Participant.append(Cycle)
            Participant.append(Running)
            totalTime = Swim + Cycle + Running

            Participant.append(totalTime)

            if totalTime > FastestParticipant[5]:
                FastestParticipant = Participant
        
            participantData.append(Participant)

            TotalTimes.append(totalTime)
        else: 
            print("Participant Too young")

            count = count - 1 # Allow them to do it again

    except ValueError:
        print("Please Enter A valid Data Type")
        count = count - 1 # Allow them to do it again

TotalTimes.sort() 

Rank = len(TotalTimes)

print("====THE RANKINGS====")
for Time in TotalTimes:
    
    for Participant in participantData:
        if Time == Participant[5] and (Participant[2] + Participant[3] + Participant[4] == Participant[5]):
            print(f"{Participant[0]} (aged {Participant[1]}), Swimming: {Participant[2]}, Cycling: {Participant[3]}, Running: {Participant[4]}, With a total Score of {Participant[5]} (Rank: {Rank}/{len(TotalTimes)})")
            Participant[5] = 0 # So that it doesnt go twice if there are two with the same score
    Rank = Rank - 1

print(f"{FastestParticipant[0]} (aged {FastestParticipant[1]}) Was the Fastest!!, Swimming: {FastestParticipant[2]}, Cycling: {FastestParticipant[3]}, Running: {FastestParticipant[4]}, With a total Score of {FastestParticipant[5]} ")

# print("PARTICIPANT DATA=====")
# print(participantData)
# print("FASTEST PARTICIPANT=====")
# print(FastestParticipant)
# print("Total Times (array)")
# print(TotalTimes)