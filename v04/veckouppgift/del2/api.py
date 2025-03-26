import requests
from typing import Any


class Api():
    
    def __init__(self, url: str) -> None:
        self._url = url


    def __call__(self) -> Any | None:
        try:
            response = requests.get(self._url)

            if response.status_code == 200:
                data = response.json()
                return data
            
            else:
                print(" > Error:", response.status_code)
                return None
        
        except requests.exceptions.RequestException as e:
            print(" > Error:", e)
            return None
        
        except:
            print(" > Error: Something else went wrong")
            return None
    

    def __del__(self):
        """
        Makes sure that the url gets destoryed
        """
        del(self._url)



if __name__ == "__main__":
    print("Wrong file")