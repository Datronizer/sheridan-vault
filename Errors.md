- [x] ⏫ Error: null value in column "sweepstakesMemberLinkId" of relation "online_venue_transaction" violates not-null constraint. This error shows when creating new account and attempting to link to a sweepstakes
	- [x] Cash In works fine.
	- [x] New fbid, ✅ 2025-05-15
	- [ ] last deposit, 
	- [ ] last cashout (members table)
		- [ ] Last Cashout Date
- [x] Launch button next to Platform button, open Sweepstakes page in new window.
- [ ] Make border for input fields thicker / more obvious
- [x] Cash In/Out missing the othe rpayment options ✅ 2025-05-14
- [ ] Have a save button / checkmark for payment section
- [x] Call Platform Username "Platform ID" instead ✅ 2025-05-15
- [x] Cash OUt needs Game Played box. Cash in doesn't need.
- [x] Tip should minus from the amount rather than add. ✅ 2025-05-15
	- [x] Amount INput => Credit Removed ✅ 2025-05-15
	- [x] Total => Total Payout ✅ 2025-05-15
	- [x] Bonus => Tip (Cash Out) ✅ 2025-05-14
- [x] Platofrm ID <=> Account name (drop the acct name column after) ✅ 2025-05-15
- [x] Remove Transaction ID column of report table ✅ 2025-05-15
- [x] Employee ID => Emplyoee Name ✅ 2025-05-15

Owner needs to see the venue dashboard  
  
Machines not needed if online venue  
  
Org has many GRs, a GR is basically 1 Venue.  
  
What does every GR need to see?  
- [ ] Members  
- [ ] Online GR dashboard  
- [ ] Tasks (Call center employees)  
  
- [ ] OGR needs back button  
  
Talk to Matt about AWS email  
  
Members functionality:  
- [ ] 7 Day report needs to be done  
- [ ] Pop up alert for first time deposit (if user is blacklisted)  
- [ ] Cash in/out form needs dedicated BACK button, or SWITCH button  
- [x] Loading blocker for cashin/out page for feedback  
- [x] Bonus text, report is gold ✅ 2025-05-17
- [x] Tips is green ✅ 2025-05-17
- [x] Remove 00 from currency in report  
- [x] Platform ID is player's username, so we can get rid of Account Name  
- [x] Page to input Platform, make current page public so admins can add new platforms  
	- [ ] Add a response to the add button  
	- [x] Creating new platforms should only be  
- [x] Assign an ID value (1,2,3, etc.) to the platform so we know which one  
	- [ ] Need a database or method to figure out what number we need
- [ ] Sweepstakes page is for venues to choose what platforms they want.  
- [ ] Sweepstakes add page is ADMIN exclusive, and it should  
- [x] Payments  
	- [x] CashApp  
	- [x] Chime  
	- [x] NextPay  
	- [x] PayPal  
	- [x] Venmo  
	- [x] Zelle  
- [x] Show Employee name instead of ID ✅ 2025-05-15
	- [ ] Need page to view all Employees  
	- [ ] Track employees' hours  
	- [ ] Employee login / logout  
- [ ] Shift Cashier is a full report of when employee logs in/out (to track hours)  
	- [ ] **Columns:** Date, Name, Login time, Logout time, Shift, Note  
- [ ] Last Deposit needs implementation  
	- [ ] "Remember sender" button to autofill payment method (can update/bind to user in separate table)  
- [ ] Make deposit Gray for first deposit row in report  
- [ ] Make Cashout banner red  
- [x] Transaction should NOT go through if value <= 0 ✅ 2025-05-15
- [x] Cash Out needs $50, $100 buttons since cashout value is 5x deposit ✅ 2025-05-15
- [x] Members List page needs to show FB ID or URL.  
	- [ ] Need to make the code more elegant. What we have right now is hacky at best.
- [x] Report only shows FB ID if user is Owner ✅ 2025-05-15
- [x] User Details also needs to show FB ID ✅ 2025-05-17
- [ ] Show how much they last deposited in UsersTable  
- [ ] Also make another column for last Cashout  
- [ ] Payment form , sweepstakes username row (auto-fill if exists)  
- [ ] Payment slip should open in new tab  
- [ ] Link tasks page to Transactions Report  
- [ ] Click on type to transfer row data to the First/returning _ Cash in/out form (future build)  
- [ ] Click on Sweepstakes name to open the sweepstakes page in new window  
- [ ] Future push notifs
- [ ] Matt has a Remember Me funciton set up for Member's login. Check that out to implement for our remember payment.