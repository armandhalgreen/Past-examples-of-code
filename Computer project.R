# 2508 Computer project

# Question 1
# Calculate phat where phat is a point estimate for the mortality rate of the surgical procedure at the hospital
p<-0.07
n<-73
d<-8
phat<-d/n 
print(phat)

# Question 2
# Generate a 1000 values from a Binomial distribution with paramters n and phat. Used the simulated random deviates to identify an approximate 95% confidence interval for the true mortality rate p
n1<-1000
print(rbinom(n1,n,phat))
quantile(rbinom(n1,n,phat),c(0.025,0.975))/n

# Question 3a
# X~ Bin(73,p)
# X is approximately distributedd with N(73p,73p(1-p))
# Check that this is a suitable approximation
x <- n*phat
x1<-n*(1-phat)
print((x >5) & (x1 >5))
# Therfore as min(np,np(1-p))>5 then the binomial distribution can be approximated with a normal distribution

# Question 3b
# Calculate a 95% confidence interval for phat
z1<-qnorm(0.025)
z2<-qnorm(0.975)
phat + c(z1,z2)*sqrt((1/n)*phat*(1-phat))

# Question 4a
# Simulate 100 samples of size n = 1000 from the population where the population is normally distributed with u=50 and sigma**2=10
u<-50
s<-sqrt(10)
n2<-1000
n3<-100
x2 <- matrix(data = rnorm(n3*n2,u,s), nrow = n3, ncol = n2)
x2


# Question 4b
# Means of each sample stored in a matrix
k=1
x3= matrix(data=NA, nrow=k, ncol=n3)
for(i in 1:n3){
  x3[k,i]=mean(x2[i,1:n2])
}

# Standard deviation of each sample stored in a matrix
k=1
x4= matrix(data=NA, nrow=k, ncol=n3)
for(i in 1:n3){
  x4[k,i]=sqrt(sum(((x2[i,1:n2])-mean((x2[i,1:n2])))^2/(length((x2[i,1:n2]))-1)))
}

# The lower value for the confidence intervals for the means
x5= matrix(data=NA, nrow=k, ncol=n3)
for(i in 1:n3){
  x5[k,i]=(mean(x2[i,1:n2])-c(qnorm(0.975))*(x4[k,i])/(sqrt(n2)))
}

# The upper value for the confidence intervals for the means
x6= matrix(data=NA, nrow=k, ncol=n3)
for(i in 1:n3){
  x6[k,i]=(mean(x2[i,1:n2])+c(qnorm(0.975))*(x4[k,i])/(sqrt(n2)))
}

# The lower and upper values for the confidence intervals for the means
x7= matrix(data=NA, nrow=n3, ncol=2)
for(i in 1:n3){x7[i,1]=(x5[1,i])}
for(i in 1:n3){x7[i,2]=(x6[1,i])}
print(x7)


# Question 4c
# Count the number of your confidence intervals that contain the true parameter value  u=50
count<-0
for(i in 1:n3){
  if(x5[k,i]<50 & x6[k,i]>50){
  count=count+1
  }
}
count
print("out of")
n3
# This value should be close to 95 as the confidence interval for each stimulated sample is 95% and there are 100 samples


# Question 4d
# Plot the 100 confidence intervals for u and u=50
install.packages("ggplot2")
ithsample<-c(1:n3)
LQ<-c(x5)
UQ<-c(x6)
u1<-c(x3)

data <- data.frame(ithsample = c(1:n3),
                   LQ<-c(x5),
                   UQ<-c(x6),
                   u1<-c(x3))

library(ggplot2)
ggplot(data, aes(ithsample, LQ)) +
  geom_errorbar(aes(ymin = LQ, ymax = UQ)) +
      labs(x = "ith sample",
           y = "mu",
           title = "Confidence interval vs ith sample") +
  geom_hline(yintercept=50)+
  geom_point(aes(ithsample,u1))+
  theme_classic()

# I tried to use for(i in 1:n3){if(UQ[i]<50|LQ[i]>50){colour="red"}} however I could not find a way to implement it in the code above


# Question 5
# The null and alternative hypothesis 
# H0:p=0.07 vs H1:p=/=0.07
# Under the null hypothesis the test statistic is T-Bin(73,0.07) which is a binomial distribution where n=73 and p=0.07 

# The crticial region values are
x8<-qbinom(0.025, n, p)
x8
x9<-qbinom(0.975, n, p)
x9


# Question 6a
# Simulate a 1000 values from the distribution of the test statistic assuming the null hypothesis is true. Then plotted these values as a histogram and x=8
x10<-c(rbinom(n2,n,0.07))
x10
hist(x10,xlab="Probability",ylab="Frequency")
abline(v=d,col="red")

# The approximate p value using the stimulated values
x11<-sort(x10)
x12<-c()

x10<-c(rbinom(n2,n,0.07))
Q1<-sort(x10)
for(i in 1:n2){if(x11[i]>8){x12[i]<-i}}
x13<-x12[which.min(x12)]
x14<-2*(1-x13/n2)
print(x14)


# Question 6b
# The exact p value using a binomial distribution
x16<-2*(1-pbinom(8,n,p))
x16


# Question 6c
# Conclusion from the hypothesis test
if(x16>0.05 & x14>0.05){print("Acept H0 at 95%")}else(print("Reject H1 at 95%"))

# As a check using the critical region
if(x8<d & x9>d){print("Accept H0 at 95%")}else{print("Reject H0 at 95%")}

# The probability of a test statistic at least as extreme as our observed value is not likely enough so accept H0
# From this we can conclude that it is moderately likely that this specific hospital's rate for this procdure is not different to the national average 


# Question 7
# Calculate the power of the hypothesis test from question 5 and 6 at p = 0.05 
x19<-pbinom(x8-1,n,0.05)+(1-pbinom(x9,n,0.05))
x19

# Calculate the power of the hypothesis test from question 5 and 6 at p = 0.7
x20<-pbinom(x8-1,n,0.7)+(1-pbinom(x9,n,0.7))
x20

# Considered many different values of p and plotted the power function of the test
x21<-c()
for(i in 1:20){(x21[i]=(pbinom(0,n,0.05*i)+(1-pbinom(10,n,0.05*i))))}
x21
i<-1:20
plot(0.05*i,x21,xlab="Probability",ylab="power function of the test")


# Question 8a
# Calculated the smallest sample size needed such that the null hypothesis in Question 5 is rejected at the 5% significance level when the mortality rate for the surgical procedure at the hospital is 10%
p1<-0.1
x22<-c()
x23<-c()

# Used a for loop to calculte the if the p value of the same of size  1 to 1000 was <0.05 and if so then stored the sample size in a vector. Also note used the floor function so that if for some sample sizes 10% of the patients does not correspond to an integer I could just take the integer part of the value as the number of deaths
for(i in 1:n2){if(2*(1-pbinom(floor(i*p1),i,p))<0.05){x22[i]<-i}}

# Used a for loop to calculte the if the p value of the same of size  1 to 1000 was <0.05 and if so then stored the p value of that sample in a vector
for(i in 1:n2){if(2*(1-pbinom(floor(i*p1),i,p))<0.05){x23[i]<-2*(1-pbinom(floor(i*p1),i,p))}}

# This is smallest sample size to give a p value <0.05
x22[which.min(x22)]
# The exact p value is
x23[which.max(x23)]


# Question 8b
# Calculated the minimum sample size that is required such that the power of the test is greater than 0.7 for all values of the true proportion p beyond 0.1 of the null hypothesis when the significance level of the test is 5%
x24<-c()
x25<-c()
x26<-c()

# Used a for loop to calculate power values for the sample sizes from 1 to 1000
for(i in 1:n2){
  
  # Calculate the lower bound of the critical region for every sample size
  x24<-(qbinom(0.025,i,p)-1)
  
  # Calculate the upper bound of the critical region for every sample size
  x25<-qbinom(0.975,i,p)
  
  # Calculate the power values of the critical region for every sample size
  power<-pbinom(x24,i,p+0.1)+(1-pbinom(x25,i,p+0.1))

#Used an if statement to store all the sample sizes where the power value>0.7
if(power>0.7){x26[i]<-i}
}
x26[which.min(x26)]


# Question 8c
# Modified the code from  question 8b to turn it into a function. The function has a single argument that is the smallest difference between the null and the true value of p
x27<-c()
x28<-c()
x29<-c()
n4<-10000

# Created a funcion with one variable dif
minimumsample<-function(dif){
  for(i in 1:n4){
    
    # Calculate the lower bound of the critical region for every sample size
    x27<-(qbinom(0.025,i,p)-1)
    
    # Calculate the upper bound of the critical region for every sample size
    x28<-qbinom(0.975,i,p)
    
    # Calculate the power values of the critical region for every sample size however this differs from question 8b because instead of +0.1 I changed it to +dif
    power<-pbinom(x27,i,p+dif)+(1-pbinom(x28,i,p+dif))
    
    #Used an if statement to stop when the power value>0.7 
    if(power>0.7){break}
  }
  
# This returns the smallest sample size
return(i)}

# The minimum sample size such that the power of the test is greater than 0.7 for all values of the true proportion p beyond 0.1
minimumsample(0.1)

# The minimum sample size such that the power of the test is greater than 0.7 for all values of the true proportion p beyond 0.05
minimumsample(0.05)

# The minimum sample size such that the power of the test is greater than 0.7 for all values of the true proportion p beyond 0.01
minimumsample(0.01)

