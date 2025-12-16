##############################################################
# What can you find here?
#
# HOW THE BONDORA DATASET WAS CREATED - FROM SCRATCH
##############################################################

# Raw data can be found and updated from
# https://www.bondora.com/cs/public-reports
# Datasets of interest are:
# Loan dataset
# Historic payments 

##############################################################
# After the download and unzip we load the 'The Loan Book'
loan <- read.csv2('C://Users//euba//OneDrive - MUNI//P2P GACR SNF//Bondora_2//LoanData//LoanData.csv',sep=',',dec='.')
# As of 22 April 2022 it had 231039 obs and 112 variables
##############################################################

##############################################################
# Remove columns that are either unnecessary or have no data in it (like Date Of Birth)
# The list of columns is as follows:
loan = loan[,-which(names(loan) %in% c('ReportAsOfEOD','LoanNumber','UserName','ContractEndDate','DateOfBirth',
                                       'County','City','EmploymentPosition','ActiveScheduleFirstPaymentReached',
                                       'PlannedPrincipalTillDate','PlannedInterestTillDate','LastPaymentOn',
                                       'CurrentDebtDaysPrimary','DebtOccuredOn','CurrentDebtDaysSecondary',
                                       'ExpectedLoss','LossGivenDefault','ExpectedReturn','ProbabilityOfDefault',
                                       'PrincipalOverdueBySchedule','PlannedPrincipalPostDefault','PlannedInterestPostDefault',
                                       'EAD1','EAD2','PrincipalRecovery','InterestRecovery','RecoveryStage','StageActiveSince',
                                       'ModelVersion','EL_V0','Rating_V0','EL_V1','Rating_V1','Restructured',
                                       'WorseLateCategory','CreditScoreEsMicroL','CreditScoreEsEquifaxRisk',
                                       'CreditScoreFiAsiakasTietoRiskGrade','CreditScoreEeMini','PrincipalPaymentsMade',
                                       'InterestAndPenaltyPaymentsMade','PrincipalWriteOffs','InterestAndPenaltyWriteOffs',
                                       'InterestAndPenaltyBalance',
                                       'GracePeriodStart','GracePeriodEnd','NextPaymentDate','NextPaymentNr','NrOfScheduledPayments','ReScheduledOn',
                                       'PrincipalDebtServicingCost','InterestAndPenaltyDebtServicingCost'))]
# Now we have only 61 variables
##############################################################

##############################################################
# Now data is going to be prepared for an analysis
##############################################################
# Convert date and time the loan is listed (on the primary market) & rename
loan$ListedOnUTC = as.Date(loan$ListedOnUTC)
names(loan)[which(names(loan)=='ListedOnUTC')] = 'date.primary'
# Convert date and time the loan is listed (on the primary market) & rename
loan$BiddingStartedOn = as.Date(loan$BiddingStartedOn)
names(loan)[which(names(loan)=='BiddingStartedOn')] = 'date.bidding'
# rename - number of bids from the internal app - 'portfolio manager', through API, manual bidding
names(loan)[which(names(loan) %in% c('BidsPortfolioManager',"BidsApi",'BidsManual'))] = c('bid.pm','bid.api','bid.man')
# Convert to 1 - new, 0 - old & rename
library(dummies)
loan$NewCreditCustomer = dummy(loan$NewCreditCustomer)[,2]
names(loan)[which(names(loan)=='NewCreditCustomer')] = 'new'
# Convert date and time & rename
loan$LoanApplicationStartedDate = as.Date(loan$LoanApplicationStartedDate)
names(loan)[which(names(loan)=='LoanApplicationStartedDate')] = 'date.application'
# Convert date and time & rename
loan$LoanDate = as.Date(loan$LoanDate)
names(loan)[which(names(loan)=='LoanDate')] = 'date.loan'
# Number of days from Loan application to Loan Bidding
loan$daystobidd = as.numeric(loan$date.bidding - loan$date.application)
# Time - trend variable - t = 1 is the oldest loan
loan$time = as.numeric(loan$date.application - min(loan$date.application))/1000
# Add squared and cube time for nonlinear effects
loan$time2 = loan$time^2
loan$time3 = loan$time^3
# Convert date and time & rename
loan$MaturityDate_Original = as.Date(loan$MaturityDate_Original)
names(loan)[which(names(loan)=='MaturityDate_Original')] = 'date.maturity'
# Convert date and time & rename
loan$MaturityDate_Last = as.Date(loan$MaturityDate_Last)
names(loan)[which(names(loan)=='MaturityDate_Last')] = 'date.maturity.last'
## Make dummies from ApplicationSignedHour - 6 hour intervals
tmp = dummy(loan$ApplicationSignedHour)
colnames(tmp) = paste('Hour.',0:23,sep='')
tmp = tmp[,-dim(tmp)[2]]
loan = data.frame(loan,tmp)
rm(tmp)
loan$ApplicationSignedHour = NULL
# Make dummies for each day
tmp = dummy(loan$ApplicationSignedWeekday); colnames(tmp) = paste('weekday.',1:7,sep='')
loan = data.frame(loan,tmp[,-7])
loan$ApplicationSignedWeekday = NULL; rm(tmp)
# Make dummies in VerificationType
tmp = dummy(loan$VerificationType); colnames(tmp) = c(paste('ver.',0:4,sep=''),'NA')
loan = data.frame(loan,tmp[,-c(1:2,6)])
# Remove loans with verification = 0 or NA -> only 58 cases
loan = loan[-which(loan$VerificationType %in% c(0,NA)),]
loan$VerificationType = NULL; rm(tmp)
# Language code dummies
tmp = dummy(loan$LanguageCode); tmp = tmp[,c(1:4,6)]; colnames(tmp) = c(paste('lang.',1:4,sep=''),'lang.6')
loan = data.frame(loan,tmp)
loan$LanguageCode = NULL
# How much is funded from the applied amount?
loan$ratio.funded = loan$AppliedAmount/loan$Amount
# Log of the applied loan amount
loan$log.app.amount = log(loan$AppliedAmount)
# Log of loan amount
loan$log.amount = log(loan$Amount)
# Make dummies from loan durations - intervals: 1-3, 4-6, 7-9, 10-12, 13-18, 19-24, 25-36, 37-48, 49-60
loan$duration.06 = (loan$LoanDuration >= 4 & loan$LoanDuration <=6)*1
loan$duration.09 = (loan$LoanDuration >= 7 & loan$LoanDuration <=9)*1 
loan$duration.12 = (loan$LoanDuration >= 10 & loan$LoanDuration <=12)*1 
loan$duration.18 = (loan$LoanDuration >= 13 & loan$LoanDuration <=18)*1 
loan$duration.24 = (loan$LoanDuration >= 19 & loan$LoanDuration <=24)*1 
loan$duration.36 = (loan$LoanDuration >= 25 & loan$LoanDuration <=36)*1 
loan$duration.48 = (loan$LoanDuration >= 37 & loan$LoanDuration <=48)*1 
loan$duration.60 = (loan$LoanDuration >= 49 & loan$LoanDuration <=60)*1 
# Log of the monthly payment
loan$log.monthly = log(loan$MonthlyPayment+1)
# Use of loan dummies
loan$use.0 = (loan$UseOfLoan == 0)*1
loan$use.1 = (loan$UseOfLoan == 1)*1
loan$use.2 = (loan$UseOfLoan == 2)*1
loan$use.3 = (loan$UseOfLoan == 3)*1
loan$use.4 = (loan$UseOfLoan == 4)*1
loan$use.5 = (loan$UseOfLoan == 5)*1
loan$use.6 = (loan$UseOfLoan == 6)*1
loan$use.7 = (loan$UseOfLoan == 7)*1
loan$use.8 = (loan$UseOfLoan == 8)*1
loan$use.m = (loan$UseOfLoan == -1)*1
loan$UseOfLoan = NULL
# Education dummies
loan$educ.2 = (loan$Education == 2)*1 
loan$educ.3 = (loan$Education == 3)*1 
loan$educ.4 = (loan$Education == 4)*1 
loan$educ.5 = (loan$Education == 5)*1 
loan$educ.6 = (loan$Education == 6)*1
# Remove loan with education '-1'
loan = loan[-which(loan$Education== -1),]
loan$Education = NULL
# Marital status dummy
loan$marital.1 = (loan$MaritalStatus == 1)*1
loan$marital.2 = (loan$MaritalStatus == 2)*1
loan$marital.3 = (loan$MaritalStatus == 3)*1
loan$marital.4 = (loan$MaritalStatus == 4)*1
loan$marital.5 = (loan$MaritalStatus == 5)*1
loan$MaritalStatus = NULL
# Number of dependants, 0, 1, 2, 3, 4, 5plus
loan$depen.0 = (loan$NrOfDependants == 0)*1
loan$depen.1 = (loan$NrOfDependants == 1)*1 
loan$depen.2 = (loan$NrOfDependants == 2)*1
loan$depen.3 = (loan$NrOfDependants == 3)*1
loan$depen.4 = (loan$NrOfDependants == 4)*1
loan$NrOfDependants = NULL
# Employment status
loan$employ.2 = (loan$EmploymentStatus == 2)*1
loan$employ.3 = (loan$EmploymentStatus == 3)*1
loan$employ.4 = (loan$EmploymentStatus == 4)*1
loan$employ.5 = (loan$EmploymentStatus == 5)*1
loan$employ.6 = (loan$EmploymentStatus == 6)*1
# Remove loans with employment status == 0
loan = loan[-which(loan$EmploymentStatus == 0), ]
loan$EmploymentStatus = NULL
# Current employment duration dummies
tmp = dummy(loan$EmploymentDurationCurrentEmployer)
colnames(tmp) = c('NA','em.dur.5p','em.dur.other','em.dur.ret','em.dur.trial',
                  'em.dur.1y','em.dur.2y','em.dur.3y','em.dur.4y','em.dur.5y')
tmp = tmp[,-1]
loan = data.frame(loan,tmp)
loan$EmploymentDurationCurrentEmployer = NULL
# Work Experience
loan$exper.02y = (loan$WorkExperience == 'LessThan2Years')*1
loan$exper.05y = (loan$WorkExperience == '2To5Years')*1
loan$exper.10y = (loan$WorkExperience == '5To10Years')*1
loan$exper.15y = (loan$WorkExperience == '10To15Years')*1
loan$exper.25y = (loan$WorkExperience == '15To25Years')*1
loan$exper.25p = (loan$WorkExperience == 'MoreThan25Years')*1
loan$WorkExperience = NULL
# Occupation area
tmp = dummy(loan$OccupationArea)
colnames(tmp) = c('m1','zero','Other','Mining','Processing','Energy','Utilities','Construction','Retail.wholesale',
                  'Transport.warehousing','Hospitality.catering','Info.telecom','Finance.insurance',
                  'Real.estate','Research','Administrative','Civil.service.military','Education',
                  'Healthcare.social.help','Art.entertainment','Agriculture.for.fish','NA')
tmp = tmp[,-which(colnames(tmp) %in% c('m1','zero','NA'))]
loan = data.frame(loan,tmp)
loan$OccupationArea = NULL
# Home ownership type
tmp = dummy(loan$HomeOwnershipType)
colnames(tmp) = c('zero','homeless','owner','livingw.parents','tenant.pfp','tenant.ufp','council.house','joint.tenant','joint.ownership','mortgage','encumbrance','other')
tmp = tmp[,-which(colnames(tmp) %in% c('zero','other'))]
loan = data.frame(loan,tmp)
rm(tmp)
# remove zero's
loan = loan[-which(loan$HomeOwnershipType == 0), ]
loan$HomeOwnershipType = NULL
# Remove loans with income total == 0 (just 4) - want to use income in denominator
loan = loan[-which(loan$IncomeTotal==0),]
# No income from principal employer dummy
loan$inc.princ.empl.no = (loan$IncomeFromPrincipalEmployer == 0)*1
# Log of (income from principal employer + 1)
loan$inc.princ.empl.l = log(loan$IncomeFromPrincipalEmployer+1)
# No income from pension
loan$inc.pension.no = (loan$IncomeFromPension == 0)*1
# Log of (income from pension + 1)
loan$inc.pension.l = log(loan$IncomeFromPension+1)
# No income from  family allowance
loan$inc.fam.all.no = (loan$IncomeFromFamilyAllowance == 0)*1
# Log of (income from  family allowance + 1)
loan$inc.fam.all.l = log(loan$IncomeFromFamilyAllowance+1)
# No income from social welfare
loan$inc.soc.wel.no = (loan$IncomeFromSocialWelfare == 0)*1
# Log of income from social welfare + 1
loan$inc.soc.wel.l = log(loan$IncomeFromSocialWelfare + 1)
# No income from leave pay
loan$inc.leave.no = (loan$IncomeFromLeavePay == 0)*1
# Log of income from leave pay + 1
loan$inc.leave.l = log(loan$IncomeFromLeavePay + 1)
# No income from child support
loan$inc.child.no = (loan$IncomeFromChildSupport == 0)*1
# Log of income fromc child support + 1
loan$inc.child.l = log(loan$IncomeFromChildSupport + 1)
# No income other
loan$inc.other.no = (loan$IncomeOther == 0)*1
# Log of other income
loan$inc.other.l = log(loan$IncomeOther + 1)
# Log of total income
loan$inc.total = log(loan$IncomeTotal + 1)
# Create dummies: 0, 1, 2, 3, 4, 5, 6-10, 10p for number of liabilities
loan$no.liab.00 = (loan$ExistingLiabilities == 0)*1
loan$no.liab.01 = (loan$ExistingLiabilities == 1)*1
loan$no.liab.02 = (loan$ExistingLiabilities == 2)*1
loan$no.liab.03 = (loan$ExistingLiabilities == 3)*1
loan$no.liab.04 = (loan$ExistingLiabilities == 4)*1
loan$no.liab.05 = (loan$ExistingLiabilities == 5)*1
loan$no.liab.10 = (loan$ExistingLiabilities >= 6 & loan$ExistingLiabilities <= 10)*1
# Log of total liabilities
loan$liab.l = log(loan$LiabilitiesTotal+1)
# Create dummies: 0, 1, 2, 3, 4, 5p for number of refinancing liabilities
loan$no.refin.00 = (loan$RefinanceLiabilities == 0)*1
loan$no.refin.01 = (loan$RefinanceLiabilities == 1)*1
loan$no.refin.02 = (loan$RefinanceLiabilities == 2)*1
loan$no.refin.03 = (loan$RefinanceLiabilities == 3)*1
loan$no.refin.04 = (loan$RefinanceLiabilities == 4)*1
# How much from total income is from 'family allowance', 'social welfare', 'child support'
loan$inc.support = (loan$IncomeFromFamilyAllowance + loan$IncomeFromSocialWelfare + loan$IncomeFromChildSupport)/loan$IncomeTotal
# Remove negative Free Cash Flow - just 22 cases
loan = loan[-which(loan$FreeCash<0),]
# Dummy Free Cash Flow = 0 or else 1
loan$FreeCash.d = (loan$FreeCash > 0)*1
# Log of free cash flow
loan$FreeCash.l = log(loan$FreeCash+1)
# Is there a default date?
loan$DefaultDate = as.Date(loan$DefaultDate)
loan$Default = (!is.na(loan$DefaultDate))*1 # table(loan$Status,loan$ActiveLateCategory,is.na(loan$DefaultDate)) # These loans are Late and some of them even repaid - but we still categorize them as Default
# What is the status of the loan
loan$Current = (loan$Status == 'Current')*1
loan$Late = (loan$Status == 'Late')*1
loan$Repaid = (loan$Status == 'Repaid')*1
# Number of previous loans before loan - dummies: 0, 1, 2, 3, 4, 5, 6, 7, 8-10, 11p
loan$no.previous.loan.00 = (loan$NoOfPreviousLoansBeforeLoan == 0)*1
loan$no.previous.loan.01 = (loan$NoOfPreviousLoansBeforeLoan == 1)*1 
loan$no.previous.loan.02 = (loan$NoOfPreviousLoansBeforeLoan == 2)*1 
loan$no.previous.loan.03 = (loan$NoOfPreviousLoansBeforeLoan == 3)*1 
loan$no.previous.loan.04 = (loan$NoOfPreviousLoansBeforeLoan == 4)*1 
loan$no.previous.loan.05 = (loan$NoOfPreviousLoansBeforeLoan == 5)*1 
loan$no.previous.loan.06 = (loan$NoOfPreviousLoansBeforeLoan == 6)*1 
loan$no.previous.loan.07 = (loan$NoOfPreviousLoansBeforeLoan == 7)*1 
loan$no.previous.loan.10 = (loan$NoOfPreviousLoansBeforeLoan > 8 & loan$NoOfPreviousLoansBeforeLoan <= 10)*1 
# Log of the amount of previous loans before loan + 1
loan$previous.loan.l  = log(loan$AmountOfPreviousLoansBeforeLoan+1)
# Number of previous early repayments
loan$no.previous.repay.00 = (loan$PreviousEarlyRepaymentsCountBeforeLoan == 0)*1
loan$no.previous.repay.01 = (loan$PreviousEarlyRepaymentsCountBeforeLoan == 1)*1
# Log of the amount of previous early repayments
loan$PreviousEarlyRepaymentsBefoleLoan[is.na(loan$PreviousEarlyRepaymentsBefoleLoan)] = 0 
loan$previous.repay.l = log(loan$PreviousEarlyRepaymentsBefoleLoan+1)
# Gender - only couple of '2' undefined
loan$Gender[loan$Gender==2] = 0
# Initial variables that are now transformed can be removed
loan$AppliedAmount = NULL
loan$Amount = NULL
loan$IncomeFromPrincipalEmployer = NULL
loan$IncomeFromPension = NULL
loan$IncomeFromFamilyAllowance = NULL
loan$IncomeFromSocialWelfare = NULL
loan$IncomeFromLeavePay = NULL
loan$IncomeFromChildSupport = NULL
loan$IncomeOther = NULL
loan$IncomeTotal = NULL
loan$ExistingLiabilities = NULL
loan$LiabilitiesTotal = NULL
loan$RefinanceLiabilities = NULL
loan$MonthlyPaymentDay = NULL
loan$DebtOccuredOnForSecondary = NULL
loan$ActiveLateCategory = NULL
loan$no.previous.loan.10 = NULL
loan$PreviousRepaymentsBeforeLoan = NULL
loan$PreviousEarlyRepaymentsBefoleLoan = NULL
loan$ActiveLateLastPaymentCategory = NULL
loan$loan$AmountOfPreviousLoansBeforeLoan = NULL
loan$PreviousEarlyRepaymentsCountBeforeLoan = NULL
loan$Status = NULL
# Remove all current loans
loan = loan[loan$Current != 1, ]

#######################################################################################################
# We have dataset of payments - useful for estimating the overall return on the loan
payment = read.csv(file='C://Users//euba//OneDrive - MUNI//P2P GACR SNF//Bondora_2//RepaymentsData//RepaymentsData.csv',sep=',',dec='.',header=T)
#######################################################################################################

#######################################################################################################
# Function that calculated Modified Internal Rate of Return
# rir - is the re-investment rate
# fic - is the FInanCing rate - it is used to bring cash-outflows to present value. However it is set to 0, because all outflows are at the beginning period.
mirr = function(cf,times,rir=0,fic=0.0245) {
  # Number of positive cash-flows
  NCF = length(cf)
  
  ########## not using this anymore
  # Instead of optimization I am interested in a heruistic (but close-enough) solution
  # Range of possible results
  # irr = seq(from=-0.99999,to=0.99999,by=0.00001)
  # NI = length(irr)
  ##########
  
  tsx = c(0,as.numeric(times[-1] - times[1]))
  
  # Find negative cash-flows and discount to the present value
  tmp = data.frame(cf,tsx)[which(cf<0),]
  # Present value of cash-flow out-flows
  PVCO = sum(abs(tmp[,1])/(1+fic)^(tmp[,2]/365))
  
  # Find positive cash-flow and compound to the future value using reinvestment rate
  tmp = data.frame(cf,tsx)[which(cf>0),]
  FVCI = sum(abs(tmp[,1])*(1+rir)^(abs(tmp[,2]-tmp[dim(tmp)[1],2])/365))
  
  # FVCI/PVCO is the return over the given period. However, I want annualized return.
  # Therefore.
  
  MIRR =  100*((FVCI/PVCO)^(365/tmp[dim(tmp)[1],2])-1)
  # Nominal profit in %
  NPRP = 100*sum(cf)/-cf[1]
  # Nominal absolute profit
  NPRA = sum(cf)
  # Future value of profit
  FVCI = FVCI-PVCO
  # Period in days
  Days = tsx[length(tsx)]
  # Check whether solution with higher days makes sense for negative IRR
  x = c(MIRR,NPRP,NPRA,FVCI,Days)
  names(x) = c("MIRR","NPRP","NPRA","FVCI","Days")
  return(x)
}

#######################################################################################################
# For each loan, let's calculate MIRR at rir = 0, while fic = 0 as all loans have only one negative CF at the beginning it does not really matter.
# We create two new columns RR1 (rate of return - 0 reinvestment rate) RR2 (rate of return - Historical reinvestment rate)
# 0 reinvestment rate
loan$RR1 = NA
# historical reinvestment rate
loan$RR2.Mean = NA
# historical median reinvestment rate
loan$RR2.Median = NA
# historical weighted average reinvestment rate
loan$RR2.WMean = NA
loan$NPRP = NA
loan$NPRA = NA
loan$FVCI = NA
loan$FVCI.Mean = NA
loan$FVCI.Median = NA
loan$FVCI.WMean = NA
loan$Days = NA
loan$end_date = NA

#######################################################################################################
# What loan rating are employed in the dataset?
table(loan$Rating,loan$Default)
# Ratings AA, A, B, C are going to be used - rest is super risky
loan = loan[loan$Rating %in% c('AA','A','B','C'),]
#######################################################################################################

#######################################################################################################
# First step - use 0 re-investment rate to find MIRR
#######################################################################################################
# Warning these lines will use parallelization
NL = dim(loan)[1]
A = Sys.time()
library(doParallel)
library(foreach)
# Number of cores
nc = 8
cl = makeCluster(nc)
registerDoParallel(cl)
MIRR.0 = foreach(i = 1:NL) %dopar% {
  # Let's match the 'id' of the 'i-th' loan to the corresponding 'payments'
  tmp = payment[which(as.character(loan$LoanId[i]) == as.character(payment$loan_id)),]
  if (dim(tmp)[1] == 0) return(rep(NA,6))
  tmp$SoS = tmp$PrincipalRepayment+tmp$InterestRepayment+tmp$LateFeesRepayment
  
  tmp$Date = as.Date(tmp$Date,format='%Y-%m-%d')
  tmp = tmp[order(tmp$Date),]
  
  cf = c(-exp(loan$log.amount[i]),tmp$SoS)
  times = c(loan$date.loan[i],tmp$Date)
  ir = mirr(cf,times=times,rir=0,fic=0)
  
  export = c()
  export[1] = ir["MIRR"]
  export[2] = ir["NPRP"]
  export[3] = ir["NPRA"]
  export[4] = ir["FVCI"]
  export[5] = ir["Days"]
  export[6] = as.Date(tmp[dim(tmp)[1],'Date'],origin='1970-01-01',format='%Y-%m-%d')
  names(export) = c('MIRR',"NPRP","NPRA","FVCI","Days",'Date')
  #save(i,file=paste('~/BrankaMarko/01 codes/tmp/',i,sep=''))
  return(export)
}
stopCluster(cl)
Sys.time()-A
# This operation took 48 minutes on 4 cores and acer swift 5 notebook
#######################################################################################################

# Now fill out the variables
for (i in 1:NL) loan[i,c('RR1','NPRP','NPRA','FVCI','Days','end_date')] = MIRR.0[[i]]
# Order loans based on the date when the loan ended
loan$end_date = as.Date(loan$end_date,origin='1970-01-01')
loan = loan[order(loan$end_date),]
# You can check the dates by plotting
# plot.ts(loan$end_date)
# plot.ts(loan$RR1)
library(zoo)
# You can check average returns over-time
x = rollmean(loan$RR1,k=1000,align='right')
plot.ts(x)

#######################################################################################################
# Create returns with non-zero re-investment rate
loan$RIR.Mean = NA
loan$RIR.Median = NA
loan$RIR.WMean = NA
# Number of cores
nc = 8
cl = makeCluster(nc)
NL = dim(loan)[1]
A = Sys.time()
cl = makeCluster(nc)
registerDoParallel(cl)
MIRR.1 = foreach(i = 1:NL) %dopar% {
  print(i)
  # Let's match the 'id' of the 'i-th' loan to the corresponding 'payments'
  tmp = payment[which(as.character(loan$LoanId[i]) == as.character(payment$loan_id)),]
  if (dim(tmp)[1] == 0) return(rep(NA,9))
  tmp$SoS = tmp$PrincipalRepayment+tmp$InterestRepayment+tmp$LateFeesRepayment
  
  tmp$Date = as.Date(tmp$Date,format='%Y-%m-%d')
  tmp = tmp[order(tmp$Date),]
  
  cf = c(-exp(loan$log.amount[i]),tmp$SoS)
  times = c(loan$date.loan[i],tmp$Date)
  
  old = loan[loan$end_date < times[1] & loan$end_date < times[1] - 365,c('RR1','log.amount')]
  old = old[complete.cases(old),]
  
  if (dim(old)[1] != 0) {
    RIR.Mean = mean(old$RR1[old$RR1 < quantile(old$RR1,p=0.99,na.rm=T)],na.rm=T)
    RR2.Mean = mirr(cf,times,rir=RIR.Mean/100,fic=0)[['MIRR']]
    FVCI.Mean = mirr(cf,times,rir=RIR.Mean/100,fic=0)[['FVCI']]
    RIR.Median = median(old$RR1,na.rm=T)
    RR2.Median =   mirr(cf,times,rir=RIR.Median/100,fic=0)[['MIRR']]
    FVCI.Median = mirr(cf,times,rir=RIR.Mean/100,fic=0)[['FVCI']]
    RIR.WMean = weighted.mean(old$RR1[old$RR1 < quantile(old$RR1,p=0.99,na.rm=T)],w=exp(old$log.amount)[old$RR1 < quantile(old$RR1,p=0.99,na.rm=T)])
    RR2.WMean =   mirr(cf,times,rir=RIR.WMean/100,fic=0)[['MIRR']]
    FVCI.WMean = mirr(cf,times,rir=RIR.Mean/100,fic=0)[['FVCI']]
    x = c(RIR.Mean,RR2.Mean,FVCI.Mean,RIR.Median,RR2.Median,FVCI.Median,RIR.WMean,RR2.WMean,FVCI.WMean)
    names(x) = c('RIR.Mean','RR2.Mean','FVCI.Mean','RIR.Median','RR2.Median','FVCI.Median','RIR.WMean',
                 'RR2.WMean','FVCI.WMean')
    return(x)
  } else {
    x = rep(NA,9)
    names(x) = c('RIR.Mean','RR2.Mean','FVCI.Mean','RIR.Median','RR2.Median','FVCI.Median','RIR.WMean',
                 'RR2.WMean','FVCI.WMean')
    return(x)
  }
}
stopCluster(cl)
Sys.time()-A
# This operation took 41 minutes on 4 physical cores (+4 virtual) and acer swift 5 notebook
#######################################################################################################

# Fill-out missing columns/variables
for (i in 1:NL) loan[i,c('RIR.Mean','RR2.Mean','FVCI.Mean','RIR.Median','RR2.Median','FVCI.Median','RIR.WMean','RR2.WMean','FVCI.WMean')] = MIRR.1[[i]]

#######################################################################################################
# ADDITIONAL TRANSFORMATIONS
# Some transformations and stuff
loan$MonthlyPayment = log(loan$MonthlyPayment + 1)
# Monthly payments to Total income
loan$PaytoIncome = log(exp(loan$MonthlyPayment)/exp(loan$inc.total))
# Rating dummies
loan$Rating = as.character(loan$Rating)
tmp = dummy(loan$Rating)
colnames(tmp) = c("A","AA","B","C")
loan = data.frame(loan,tmp)
loan = loan[order(loan$date.loan),]
# Rename Default
names(loan)[which(names(loan) == 'Default')] = 'default'
# Calculate simplified annualized nominal profit
loan$return = ((loan$FVCI+exp(loan$log.amount))/exp(loan$log.amount))^(1/(loan$Days/365))-1
#######################################################################################################

# Make a neat version of the database with nicer variable arrangement (Date loan start, Date loan end, default, return, explanatory only)
bondora = loan[,c('date.loan','date.maturity.last','default','return',
                  'RR1','RR2.Mean','RR2.Median','RR2.WMean','NPRP','NPRA','FVCI','FVCI.Mean','FVCI.Median','FVCI.WMean',
                  'new','Age','Gender','Interest',
                  'MonthlyPayment','DebtToIncome','NoOfPreviousLoansBeforeLoan','AmountOfPreviousLoansBeforeLoan',
                  'time','time2','time3','Hour.0','Hour.1','Hour.2','Hour.3','Hour.4','Hour.5','Hour.6','Hour.7','Hour.8',
                  'Hour.9','Hour.10','Hour.11','Hour.12','Hour.13','Hour.14','Hour.15','Hour.16','Hour.17','Hour.18',
                  'Hour.19','Hour.20','Hour.21','Hour.22','weekday.1','weekday.2','weekday.3','weekday.4','weekday.5','weekday.6',
                  'ver.2','ver.3','ver.4','lang.1','lang.2','lang.3','lang.4','lang.6',
                  'log.amount','duration.06','duration.09','duration.12','duration.18',
                  'duration.24','duration.36','duration.48','duration.60',
                  'use.0','use.1','use.2','use.3','use.4','use.5','use.6','use.7','use.8','use.m',
                  'educ.2','educ.3','educ.4','educ.5','educ.6','marital.1','marital.2','marital.3','marital.4','marital.5',
                  'depen.0','depen.1','depen.2','depen.3','depen.4','employ.2','employ.3','employ.4','employ.5','employ.6',
                  'em.dur.5p','em.dur.other','em.dur.ret','em.dur.trial','em.dur.1y','em.dur.2y',
                  'em.dur.3y','em.dur.4y','em.dur.5y','exper.02y','exper.05y','exper.10y','exper.15y',
                  'exper.25y','exper.25p','Other','Mining','Processing','Energy','Utilities','Construction',
                  'Retail.wholesale','Transport.warehousing','Hospitality.catering','Info.telecom','Finance.insurance',
                  'Real.estate','Research','Administrative','Civil.service.military','Education','Healthcare.social.help',
                  'Art.entertainment','Agriculture.for.fish','homeless','owner','livingw.parents','tenant.pfp',
                  'council.house','joint.tenant','joint.ownership','mortgage','encumbrance','inc.princ.empl.no',
                  'inc.princ.empl.l','inc.pension.no','inc.pension.l','inc.fam.all.no','inc.fam.all.l',
                  'inc.soc.wel.no','inc.soc.wel.l','inc.leave.no','inc.leave.l','inc.child.no','inc.child.l',
                  'inc.other.no','inc.other.l','inc.total','no.liab.00','no.liab.01','no.liab.02','no.liab.03',
                  'no.liab.04','no.liab.05','no.liab.10','liab.l','no.refin.00','no.refin.01','no.refin.02',
                  'no.refin.03','no.refin.04','inc.support','FreeCash.d','FreeCash.l','no.previous.loan.00',
                  'no.previous.loan.01','no.previous.loan.02','no.previous.loan.03','no.previous.loan.04',
                  'no.previous.loan.05','no.previous.loan.06','no.previous.loan.07','previous.loan.l','no.previous.repay.00',
                  'no.previous.repay.01','previous.repay.l','A','AA','B','C')]
names(bondora)[1] = 'date.start'
names(bondora)[2] = 'date.end'
rm(cl,MIRR.0,MIRR.1,old,payment,tmp,A,cf,i,nc,NL,times,x,mirr)
#######################################################################################################
# Check missing values across variables
apply(bondora[,-c(1,2)],2,function(x) sum(is.na(x)))

#######################################################################################################
# Store the dataset
save(bondora,file='C://Users//euba//OneDrive - MUNI//P2P GACR SNF//Bondora_2//Bondora')
# For compatibility - save image and specify a version! ?save.image
# save.image(bondora,file='G://Grants//GACR SNF 2021//data//Bondora//Bondora', version)
# For Python users
library(feather)
write_feather(bondora,"C://Users//euba//OneDrive - MUNI//P2P GACR SNF//Bondora_2//Bondora.feather")
