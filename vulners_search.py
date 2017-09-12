## Text menu in Python
import vulners
vulners_api = vulners.Vulners()

def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Database Search"
    print "2. CVE Search"
    print "3. Public Exploit Search"
    print "4. Software Vulnerability Search"
    print "5. Exit"
    print 67 * "-"

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
    if choice==1:
	print "Search for Vuln:",
	filename = raw_input()
	search_result = vulners_api.search(filename, limit=10)
	print search_result
    elif choice==2:
        print "Search for a CVE-xxx-xxx"
	filename = raw_input()
	cve_search = vulners_api.document(filename)
	print cve_search
    elif choice==3:
        print "Search for a public exploit"
	filename = raw_input()
	search_exploits = vulners_api.searchExploit(filename)
	print search_exploits
        ## You can add your code or functions here
    elif choice==4:
        print "Search for software exploit by version number e.g httpd 1.5"
	print "Enter software e.g Adobe"
	filename = raw_input()
	print "Enter version number e.g 22"
	filename2 = raw_input() 
	results = vulners_api.softwareVulnerabilities(filename, filename2)
	exploit_list = results.get('exploit')
	vulnerabilities_list = [results.get(key) for key in results if key not in ['info', 'blog', 'bugbounty']]
	print  exploit_list
    elif choice==5:
        print "Menu 5 has been selected"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
