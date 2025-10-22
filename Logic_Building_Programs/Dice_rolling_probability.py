import random
from tqdm import tqdm

#Defining the constants
N_TRIALS=1000000  # This is experimental like how many times we roll the dice
TARGET_SUM=7   # Target sum to check for

def roll_die():
    """Simulates rolling a single six-sided die."""
    return random.randint(1, 6)
def run_experiment():
    #This rolls two dice and return theri sum"
    die1=roll_die()
    die2=roll_die()

    return die1 + die2
def main():
    #counting how many times we get our target sum
    count_target=0
    print(f"Rolling two dice {N_TRIALS} times")


    #Repeat the experiment many times
    for i in tqdm(range(N_TRIALS)):
        total=run_experiment()

        #check if we got the target sum
        if total==TARGET_SUM:
            count_target += 1
    #Calculating the probability
    #probability=times we got 7/total rolls
    probabaility=count_target / N_TRIALS

    print(f"\n===Results===")
    print(f"Times we rolled sum= {TARGET_SUM}: {count_target}  out of {N_TRIALS} rolls")
    print(f"Estimated Probability of rolling is {probabaility:.6f}")
    
if __name__ == "__main__":
    main()