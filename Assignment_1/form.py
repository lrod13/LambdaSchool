import requests

contact_info = {
	"email": "test@test.com",
	"lastname": "test",
	"message": "just testing",
	"name": "test"
}

r = requests.post("https://lambdaschool.com/contact-form", json = contact_info)

print("response: %s status code %s" % (r.text, r.status_code))