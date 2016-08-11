import os

VON_BASE_PATH = "/home/evan/Dropbox/OlyBase/" # TODO for public, use better
VON_INDEX_NAME = "index"
VON_INDEX_PATH = os.path.join(VON_BASE_PATH, VON_INDEX_NAME)
VON_CACHE_NAME = "cache"
VON_CACHE_PATH = os.path.join(VON_BASE_PATH, VON_CACHE_NAME)

EDITOR = os.environ.get('EDITOR','vim') # that easy!

SEPERATOR = '\n---\n'
NSEPERATOR = '\n' + SEPERATOR + '\n'

TAG_HINT_TEXT = """# Some hints for tags:
#
# *** Difficulty: @trivial @aleph @bet @dalet @gimel @zayin @yod @kurumi
# *** Sources: @mine @obscure @rare @secret @exam @blind @well
# *** Problem Shape: @yesno @find @construct @bestpossible @hardanswer @aime
# (here @well means I spent a lot of time on the problem myself)
#
# Quality: @favorite > @nice > @good > @ugly @work
# Philosophy: @instructive @reliable @justdoit @magic
# Philosophy': @smallcases @equalitycase @scouting @meta @dumb
# Philosophy'': @wishful @criticalclaim @stronger @thinkbig
# Solution Method: @induct @manysolutions @magic @inefficient @explicit @compute
# More tags: @pitfall @troll @intuitive @size @weak @maturity
#
# NT:    @primes @p-adic @QR @pell @smallestprime @mods
#        @fermat @zsig @cyclotomic @divis @order @christmas @CRT
# Alg:   @polynomial @trig @roots @calculus
#        @continuity @irreducible @exactsum @manip
# Ineq:  @holder @CDN @schur @AMGM @Titu @homogenize
#        @dehomogenize @SOS @jensen @isofudge
# Combo: @greedy @optimization @additivecombo @extreme @invariant
#        @free @pigeonhole @parity @graph @adhoc @EV @combogeo
#        @hall @grid @rigid @perturb @algorithm
# Geometry tags
  # Part I and II: @anglechase @simtri @pop @homothety
  #                @cevalaus @trig @complex @bary @length
  # Part III:      @inversion @polar @projective @harmonic
  #                0@miquel @spiralsim @mixtilinear"""

USE_COLOR = True
KEY_CHAR = 'C~'

DIFFS= ['trivial', 'aleph', 'bet', 'dalet', 'gimel', 
		'zayin', 'yod', 'kurumi']
