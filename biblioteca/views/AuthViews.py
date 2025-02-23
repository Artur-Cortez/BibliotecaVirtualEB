from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from models import Usuario
from forms import LoginForm, SignupForm



class AuthViews:

    def login_view(request):
        message = None
        if request.user.is_authenticated:
            return redirect('/')
                
        if request.method == 'POST':
            loginForm = LoginForm(request.POST)
            if loginForm.is_valid():
                user = authenticate(
                    request,
                    username=loginForm.cleaned_data['login'],
                    password=loginForm.cleaned_data['password']
                )
                if user is not None:
                    login(request, user)
                    next_url = request.GET.get('next', '/')
                    return redirect(next_url)
                else:
                    message = {'type': 'error', 'text': 'Email e/ou senha inválidos!'}
        else:
            loginForm = LoginForm()

        response = render(request, 'auth/login.html', {
            'form': loginForm, 
            'message': message,
            'title': 'Login',
            'button_text': 'Entrar',
            'link_text': 'Registrar', 
            'link_href': '/register'
        })

        return response
    
    def signup_view(request):
        registerForm = SignupForm()
        message = None
        if request.user.is_authenticated:
            return redirect('/')
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            registerForm = SignupForm(request.POST)
        
            if registerForm.is_valid():
                verifyUsername = Usuario.objects.filter(username=username).first()
                verifyEmail = Usuario.objects.filter(email=email).first()
                if verifyUsername is not None:
                    message = {'type': 'danger', 'text': 'Já existe um usuário com este username!'}
                elif verifyEmail is not None:
                    message = {'type': 'danger', 'text': 'Já existe um usuário com este e-mail!'}
                else:     
                    user = Usuario.objects.create_user(username=username, email=email, password=password)
                    registerForm.signup(request, user)
                    if user is not None:
                        message = {'type': 'success', 'text': 'Conta criada com sucesso!'}
                        next = request.GET.get('next')
                        if next:
                            return redirect(next)      
                    else:
                        message = {'type': 'danger', 'text': 'Um erro ocorreu ao tentar criar o usuário.'}
                    
        context = {'form': registerForm, 'message': message, 'title': 'Registrar', 'button_text': 'Registrar', 'link_text': 'Login', 'link_href': '/login'}
        return render(request, template_name='account/signup.html', context=context, status=200)
    
    def logout_view(request):
        logout(request)
        return redirect('/')    
    
