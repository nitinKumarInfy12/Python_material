import csv
import boto3
import gspread
import jinja2
from oauth2client.service_account import ServiceAccountCredentials

AWS_PROFILE = "INSERT-AWS-PROFILE-HERE"
BUCKET = "INSERT-BUCKET-NAME-HERE"
WORKBOOK = "INSERT-WORKBOOK-NAME-HERE"


def download_data():
    """Download data using the Google Sheets API"""
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )
    client = gspread.authorize(credentials)

    worksheet = client.open(WORKBOOK).get_worksheet(0)
    sheet_values = worksheet.get_all_values()

    print(f"Downloading: {worksheet.title}")
    with open("my_pokemon_stats.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(sheet_values)


def generate_site():
    """Generate site in local directory"""
    print("Process data and build site")

    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("template.html")

    with open("my_pokemon_stats.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    output = template.render(data=data)

    with open("index.html", "w") as f:
        f.write(output)


def deploy_site():
    """Deploy site S3 bucket"""
    print("Upload data to S3")
    session = boto3.Session(profile_name=AWS_PROFILE)
    s3 = session.resource("s3")
    s3.Bucket(BUCKET).upload_file(
        Filename="index.html", Key="index.html", ExtraArgs={"ContentType": "text/html"}
    )


if __name__ == "__main__":
    download_data()
    generate_site()
    deploy_site()