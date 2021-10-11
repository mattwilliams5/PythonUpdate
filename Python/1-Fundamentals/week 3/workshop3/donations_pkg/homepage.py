def show_homepage():
    """
       Display basic menu
    """

    print(""" === DonateMe Homepage ===
          --------------------------------
          |1. Login     |2. Register      |
          --------------------------------
          |3. Donate   |4. Show Donations|
          --------------------------------
          |            5. Exit             |
          --------------------------------


          """)


def donate(username):
    """
       Get the dollar amount for
       donation
    """

    donation_amt = input("Enter amount to donate: ")
    donation = float(donation_amt)
    print("\n", username, "donated", donation)
    return donation


def show_donations(donations):
    """
        Get total sum of users
        donations
    """
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
        return ""
    else:
        for item in donations:
            print(item)
