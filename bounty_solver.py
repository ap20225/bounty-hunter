def solve_bounty(bounty_amount):
    """
    Simulates solving a bounty by returning a success message.
    
    Args:
        bounty_amount (int): The amount of the bounty to solve
    
    Returns:
        str: A success message indicating the bounty was solved
    """
    return f"Bounty of ${bounty_amount} solved successfully!"

def calculate_reward(bounty_amount, difficulty=1):
    """
    Calculates reward based on bounty amount and difficulty.
    
    Args:
        bounty_amount (int): The base bounty amount
        difficulty (int): Difficulty level (default: 1)
    
    Returns:
        int: Calculated reward amount
    """
    return bounty_amount * difficulty
