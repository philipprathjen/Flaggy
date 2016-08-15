import os, sys, django
sys.path.append("/Users/philipp_rathjen/Documents/Work/Flaggy/flaggy/src")
os.environ["DJANGO_SETTINGS_MODULE"] = "flaggy.settings"
django.setup()

from profiles.models import Country

country_dict = {
	"AF": "Afghanistan",
	"AX": "Aland Islands",
	"AL": "Albania",
	"DZ": "Algeria",
	"AS": "American Samoa",
	"AD": "Andorra",
	"AO": "Angola",
	"AI": "Anguilla",
	"AQ": "Antarctica",
	"AG": "Antigua and Barbuda",
	"AR": "Argentina",
	"AM": "Armenia",
	"AW": "Aruba",
	"AU": "Australia",
	"AT": "Austria",
	"AZ": "Azerbaijan",
	"BS": "Bahamas",
	"BH": "Bahrain",
	"BD": "Bangladesh",
	"BB": "Barbados",
	"BY": "Belarus",
	"BE": "Belgium",
	"BZ": "Belize",
	"BJ": "Benin",
	"BM": "Bermuda",
	"BT": "Bhutan",
	"BO": "Bolivia, Plurinational State of",
	"BQ": "Bonaire, Sint Eustatius and Saba",
	"BA": "Bosnia and Herzegovina",
	"BW": "Botswana",
	"BV": "Bouvet Island",
	"BR": "Brazil",
	"IO": "British Indian Ocean Territory",
	"BN": "Brunei Darussalam",
	"BG": "Bulgaria",
	"BF": "Burkina Faso",
	"BI": "Burundi",
	"KH": "Cambodia",
	"CM": "Cameroon",
	"CA": "Canada",
	"CV": "Cape Verde",
	"KY": "Cayman Islands",
	"CF": "Central African Republic",
	"TD": "Chad",
	"CL": "Chile",
	"CN": "China",
	"CX": "Christmas Island",
	"CC": "Cocos (Keeling) Islands",
	"CO": "Colombia",
	"KM": "Comoros",
	"CG": "Congo",
	"CD": "Congo, the Democratic Republic of the",
	"CK": "Cook Islands",
	"CR": "Costa Rica",
	"CI": "Cote d'Ivoire",
	"HR": "Croatia",
	"CU": "Cuba",
	"CW": "Curacao",
	"CY": "Cyprus",
	"CZ": "Czech Republic",
	"DK": "Denmark",



}


print(country_dict)