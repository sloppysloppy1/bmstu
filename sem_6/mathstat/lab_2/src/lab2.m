function lab2()
    clear all;

    X = [-17.04,-18.29,-17.38,-18.11,-18.96,-17.65,-17.02,-17.22,-16.25,-17.44,-17.69,-17.61,-17.09,-17.19,-16.02,-17.56,-16.94,-17.29,-16.93,-16.61,-19.38,-17.53,-16.39,-17.89,-17.98,-17.04,-16.22,-19.09,-18.91,-17.77,-18.30,-17.44,-18.84,-16.39,-16.13,-18.37,-16.37,-16.70,-17.78,-17.03,-17.76,-17.87,-17.20,-18.44,-17.19,-17.75,-16.81,-17.97,-18.03,-16.87,-16.10,-19.16,-16.51,-18.39,-16.48,-18.08,-17.49,-18.89,-19.09,-17.96,-18.40,-16.96,-18.15,-18.71,-17.81,-17.86,-19.47,-17.86,-17.60,-17.30,-17.60,-17.71,-18.42,-16.88,-16.76,-18.00,-17.97,-16.83,-18.00,-18.08,-17.61,-17.02,-16.73,-17.64,-18.76,-17.68,-18.04,-16.45,-18.79,-18.03,-17.38,-15.27,-15.97,-17.41,-18.61,-18.00,-17.42,-17.77,-19.05,-16.16,-16.27,-18.00,-18.90,-17.05,-17.46,-17.49,-18.20,-17.59,-15.78,-18.88,-18.53,-17.39,-17.83,-18.17,-16.15,-17.66,-17.76,-18.32,-17.70,-17.56];

    %nachinaem s 10 znacheniya, chtobi grafiki viglyadeli adekvatnee
    N = 10:120;
    gamma = 0.9;
    
    alpha = (1 - gamma)/2;

    %vichislenye MX i DX
    mu = mean(X);
    sSqr = var(X);
    
    fprintf('mu = %.2f\n', mu); 
    fprintf('S^2 = %.2f\n\n', sSqr);
    
    %vichislenye tochechnih ocenok MX i DX
    muArray = [];
    for i = N
        muArray = [muArray, mean(X(1:i))];
    end
    
    varArray = [];
    for i = N
        varArray = [varArray, var(X(1:i))];
    end
 
    figure
    plot([N(1), N(end)], [mu, mu], 'm');
    hold on;
    plot(N, muArray, 'g');
    
    %zapolenie massivov dlya postoeniya grafikov
    %mu^(x_n), mu_down(x_n), mu_up(x_n) 
    Ml = muArray - sqrt(varArray./N).*tinv(1 - alpha, N - 1);
    plot(N, Ml, 'b');
    
    Mh = muArray + sqrt(varArray./N).*tinv(1 - alpha, N - 1);
    plot(N, Mh, 'r');
    grid on;
    hold off;

    fprintf('mu_low = %.2f\n', Ml(end));
    fprintf('mu_high = %.2f\n', Mh(end));

    figure
    plot([N(1), N(end)], [sSqr, sSqr], 'm');
    hold on;
    plot(N, varArray, 'g');
    
    %zapolenie massivov dlya postoeniya grafikov
    %S2(x_n), sigma_down(x_n), sigma_up(x_n)  
    Sl = varArray.*(N - 1)./chi2inv(1 - alpha, N - 1);
    plot(N, Sl, 'b');
    
    Sh = varArray.*(N - 1)./chi2inv(alpha, N - 1);
    plot(N, Sh, 'r');
    grid on;
    hold off;
    fprintf('sigma^2_low = %.2f\n', Sl(end));
    fprintf('sigma^2_high = %.2f\n', Sh(end));
end