# Web Automation - Python + Pytest + POM + Selenium + Allure

## Package Installation

```sh
pip install -r requirements.txt
```

## How to Run
### Pytest

```sh
pytest --browser={브라우저명(chrome,IE,FireFox)} --alluredir={결과 생성 폴더} --id={user.id} --password={user.password}
```

### Allure Report

```sh
allure serve {결과 생성 폴더}
```
