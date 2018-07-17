# Django REST Framework - Account

**Account APP for Django REST Framework with API Views.**<br>

`DRF Account` is a Django app that for maintaining Account Information. This app is majorly being used in
[Vitartha's](https://vitartha.com) product [Hisab Kitab](https://hisabkitab.in)

#### Contributors

- **[Civil Machines Technologies Private Limited](https://github.com/civilmahines)**: For providing me platform and 
funds for research work. This project is hosted currently with `CMT` only. 
- [Himanshu Shankar](https://github.com/iamhssingh): The app was initiated and worked upon majorly by Himanshu. This app
is currently in use in various other django projects that are developed by him.

**We're looking for someone who can contribute on docs part**

#### Installation

- Download and Install via `pip`
```
pip install drf_account
```
or<br>
Download and Install via `easy_install`
```
easy_install drf_account
```
- Add `drf_user` in `INSTALLED_APPS`<br>
```
INSTALLED_APPS = [
    ...
    'drf_account',
    ...
]
```
- Include urls of `drf_account` in `urls.py`
```
urlpatterns = [
    ...
    path('/api/account/', include('drf_account.urls')),
    ...
]

# or

urlpatterns = [
    ...
    url(r'api/account/', include('drf_account.urls')),
    ...
]
```

- Finally, run `migrate` command
```
python manage.py migrate drf_account
```
