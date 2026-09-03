error=int(input("200,301,404,500,503 this are the error if you want to known about this error enter number:"))

match error:
    case 200:
        print("200 OK → Request successful.")
    case 301:
        print("301 Moved Permanently → Resource moved to a new URL permanently.")
    case 404:
        print("404 Not Found → Resource not found.")
    case 500:
        print("500 Internal Server Error → Generic server error.")
    case 503:
        print("503 Service Unavailable → Server temporarily overloaded or under maintenance.")
    case _:
        print("Error Not identify")
