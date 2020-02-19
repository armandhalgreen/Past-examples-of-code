# I confirm that this repository is the work of our team, except where clearly indicated in the text

#function for the expectation step, which returns a matrix containing the probability of each fish length of belonging to each of age groups
posterior_probability <- function(dataset, estimates = data.frame(c(0,0,0), c(1,1,1), c(0.5,0.5,0.5))){
  #error trap for invalid arguments
  if(!is.data.frame(dataset) | !is.data.frame(estimates)) stop("invalid arguments in posterior_probability")
  mean_vec <- estimates[ ,1] #initializing a vector containing the means of the three age groups
  sigma_vec <- estimates[ ,2] #initializing a vector containing the standard deviations of the three age groups
  posterior <- matrix(,nrow = length(dataset[,2]), ncol = 3) #initializing an empty matrix (hence the yellow error) to be filled with each posterior probabilities
  #rows are for the entries y_i
  #columns are for their posterior coresponding to each age group 1,2 or 3
  for (i in 1:length(dataset[,2])) {
    for (k in 1:3) {
      #the for loops are running through the lengths and the age groups in oder to fill the matrix
      posterior[i,k] <- ((dnorm(dataset$Length[i], mean_vec[k], sigma_vec[k])*(length(which(dataset$Age == k))/length(dataset$Age)))/ #P(yi|yi in k)*P(k)
                           #the next bit is the sum representing the denominator P(y_i)
                           (dnorm(dataset$Length[i], mean_vec[1], sigma_vec[1])*(length(which(dataset$Age == 1))/length(dataset$Age))+
                              dnorm(dataset$Length[i], mean_vec[2], sigma_vec[2])*(length(which(dataset$Age == 2))/length(dataset$Age))+
                              dnorm(dataset$Length[i], mean_vec[3], sigma_vec[3])*(length(which(dataset$Age == 3))/length(dataset$Age))))
    }
  }
  dataf_post <- (data.frame(posterior)) #output as to be a dataframe with the age group as columns
  colnames(dataf_post) <- c("Age1", "Age2", "Age3") 
  return(dataf_post)
}

#writing the maximisation function which updates the values for the mean, standard deviation and lambda estimates
maximisation <- function(dataset, posterior){
  #error trap for invalid arguments on maximisation
  if(!is.data.frame(dataset) | !is.data.frame(posterior)) stop("invalid arguments in maximisation")
  #initializing the mean, standard deviation and lambda vectors for the new estimates
  mean_vec <- rep(0, 3)
  sigma_vec <- rep(0, 3)
  lambda_vec <- rep(0, 3)
  #the denominator for the mean and variance also appears in the lamdba function, thus it is worth computing separately
  denominator_vec <- rep(0, 3)
  for (k in 1:3) {
    denominator_vec[k] <- sum(posterior[,k])
    #calculate estimated mean for each age group
    numerator1 <- sum(posterior[,k]*dataset$Length) #computing the numerator as the sum of posterior times the fish lengths
    mean_vec[k] <- numerator1/denominator_vec[k] #putting together our numerator and denominator for each age group
    #calculate estimated sigma for each age group 
    numerator2 <- sum(posterior[,k]*(dataset$Length-rep(mean_vec[k], length(dataset$Length)))^2) #same as above, but we are multiplying by the squared distance from the mean
    sigma_vec[k] <- sqrt(numerator2/denominator_vec[k]) #assembling the final formula
    #calculate estimated lambda for each age group
    lambda_vec[k] <- denominator_vec[k]/length(dataset$Length)
  }
  #construct a data frame for estimates with the row the age groups and the column the values for mean, sd and lambda
  estimates <- data.frame(mean_vec, sigma_vec, lambda_vec)  
  rownames(estimates) <- c("Age1", "Age2", "Age3")
  colnames(estimates) <- c("mu", "sigma", "lambda")
  return(estimates)
}

#computing the likelihood, which is going to be used in the convergence step
likelihood <- function(dataset, estimates = data.frame(c(0,0,0), c(1,1,1), c(0.5,0.5,0.5))){
  #error trap for invalid arguments
  if(!is.data.frame(dataset) | !is.data.frame(estimates)) stop("invalid arguments in likelihood")
  #initializing the mean, standard deviation and lamdba vectors from the estimates for clarity
  mean_vec <- estimates[ ,1]
  sigma_vec <- estimates[ ,2]
  lambda_vec <- estimates[ ,3]
  log_likelihood <- 0 #initializing log_likelihood with 0 as it is going to be part of a sum 
  for (i in 1:length(dataset$Length)){   #iterate N times to obtain likelihood
    sum1 <- 0 #initializing the inner sum with 0 and using sum1 to avoid confusion with the function sum()
    for (k in 1:3){   #iterate 3 times to get the sum, for age group 1, 2, 3
      sum1 <- sum1 + lambda_vec[k]*dnorm(dataset$Length[i], mean_vec[k], (sigma_vec[k]^2))
      #lambda_vec[j] is the estimate of lambda for group k (k = 1,2,3), similar to mean_vec and sigma_vec
    }
    log_likelihood <- log_likelihood + log(sum1)  #using log properties to avoid errors caused by extreme values
  }
  return(log_likelihood)
}

#putting everything together in the main function
teamEM <- function(dataset, epsilon = 10^(-8), maxit = 1000){
  #error trap for invalid arguments
  if(!is.data.frame(dataset) | !is.numeric(epsilon) | !is.numeric(maxit)) stop("invalid arguments in teamEM")
  #Initialization
  #finding the borders between age groups aka finding the max of group 1 and max of group 2 and initializing said borders
  m_1 <- 0
  m_2 <- 0
  for (i in 1:length(dataset$Age)) {
    if (!is.na(dataset$Age[i])){ #testing if the groups have been assigned
      if(dataset$Age[i] == 1){ #testing if the fish is in the first group
        if(dataset$Length[i] > m_1){
          m_1 <- dataset$Length[i] #updating maximum if the length is bigger than the previous max
        }
      } else if (dataset$Age[i] == 2){ #testing if the fish is in the second group
        if(dataset$Length[i] > m_2){
          m_2 <- dataset$Length[i] #updating maximum if the length is bigger than the previous max  
        }
      } 
    }
  }
  #assigning Age groups to the NA ones
  for (i in 1:length(dataset$Age)) {
    if (is.na(dataset$Age[i])){ #checking if the Age group is not assigned
      if (dataset$Length[i] <= m_1){
        dataset$Age[i] <- 1 #checking if the length is smaller than the first border to assign the fish there
      } else if (dataset$Length[i] <= m_2) {
        dataset$Age[i] <- 2 #otherwise, we are checking if the length is smaller than the second border to assign the fish there
      } else if (dataset$Length[i] > m_2) {
        dataset$Age[i] <- 3 #if the fish is longer than the second border, it belongs to the third group
      }
    }
  }
  #initializing the mean, sigma and lambda vectors with 0
  mean_vec <- rep(0,3)
  sigma_vec <- rep(0,3)
  lambda_vec <- rep(0,3)
  #computing the initial values for the mean, sigma and lambda for each group
  for (k in 1:3){
    #computes the mean of each group
    mean_vec[k] <- mean(dataset$Length[which(dataset$Age == k)])
    #computes the standard deviation of each group
    sigma_vec[k] <-  sqrt(var(dataset$Length[which(dataset$Age == k)]))
    #computes the number of elements in each group divided by total number of observations (aka 1000) as the initial lambda
    lambda_vec[k] <- length(which(dataset$Age == k))/length(dataset$Age)
  }
  #defining the inits dataframe for the output and further analysis
  inits <- data.frame("mu" = mean_vec, "sigma" = sigma_vec, "lambda" = lambda_vec)
  rownames(inits) <- c("Age1", "Age2", "Age3")
  estimates <- inits #initializing estimates with the inits data frame
  posterior <- NA #initializing the posterior data frame 
  likelihood_vec <- c() #initializing the vector containing all of the log-likelihoods
  converge <- FALSE #setting convergence boolean check to FALSE
  count <- 1 #setting up a count to check that we have not reached the maximum number of iterations
  #repeating the algorithm until we reach the maxit value or the estimates converge
  while (count <= maxit && converge == FALSE){
    posterior <- posterior_probability(dataset, estimates) #data frame generated by the posterior_probability function
    estimates <- maximisation(dataset, posterior) #updating the mean, standard deviation and lambda estimates with the maximisation function
    #checking if we are at least on the second iteration in order to have previous likelihood to compare with
    #convergence check
    if (count > 1 && abs(likelihood(dataset, estimates) - likelihood_vec[length(likelihood_vec)]) < epsilon) converge <- TRUE
    likelihood_vec <- c(likelihood_vec, likelihood(dataset, estimates)) #adding the new likelihood value to the vector
    count <- count + 1 #updating the iteration counter
  }
  #returning the final estimates, initial values, covergence check, data frame of posterior probabilities and vector of likelihood values
  return(list( estimates = estimates , inits= inits, converged = converge, posterior = posterior, likelihood = likelihood_vec))
}
