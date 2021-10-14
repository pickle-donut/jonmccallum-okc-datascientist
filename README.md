# jonmccallum-okc-datascientist

## Personality Test
https://www.16personalities.com/enfj-personality

I feel that the test results resonate with my own internal perception of myself.
I genuinely try and do the right thing, and I have had many of my peers remark that they feel I am a natural leader.
The last time I took a Myers Briggs personality test, I was denoted as an ENTJ so this result is also not far off from previous assessments.

## Free Response Question

I work best when I am immersed in a technically diverse team working interesting problems.
I prefer to feel proficient in the technolgies employed to deliver technical solutions; not just thrusted into some new tech stack to apply to some project with encroaching deadlines.
I prefer support and autonomy from my management team, but welcome involvement as requirements evolve.
I prefer work-life balance, but I can stretch to adhere to necessary time commitments.
I prefer to lessen travel as much as possible given the current world health environment.

## Challenge #1

During EDA, the original data set was reduced to the following columns:

**price** \
**para1** \
**loc1_0** \
**loc1_1** \
**loc1_2** \
**loc1_3** \
**loc1_6** \
**loc1_7** \
**dow_Mon** \
**dow_Thu** \
**dow_Tue**

This was achieved via one-hot encoding discrete fields using a combination of correlation matrices, k-means, PCA, and Factor Analysis.

With this refined set, a simple linear regression model is constructed to achieve a baseline.
Finally, a grid search operation over several different models is attempted to see if a better fit than the baseline can be achieved.
Unfortunately, given time commitments, the baseline model (linear regression) is the best that could be achieved.
The results are as below:

**-- MODEL RESULTS --** \
Tuned Model: **linear-regression** \
MAPE on Train Set: **60.7369** \
MAPE on Test Set: **62.8417** \
R2 on Test Set: **0.0894**

The relatively low R^2 indicates a poor fit for this model.
There could be a number of reasons for this...

1. The sample trained on was a random sampling of 500 records (other sampling methods and in great counts counts should be explored to try and achieve a better fit).
2. The data was scaled to a mean=0 and stddev=1 (other scaling methods should be explored to try and achieve a better fit).
3. Hasty assumptions on relevant features based on purely computational outputs (missing potentially interaction terms, domain-specific knowledge).
4. Lack of feature engineering (adding additional features should be explored to try and achieve a better fit).

