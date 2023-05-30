<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Have I Been Pwned: Pwned Passwords</title>
<meta property="og:title" content="Have I Been Pwned: Pwned Passwords" />
<meta name="description" content="Have I Been Pwned allows you to search across multiple data breaches to see if your email address or phone number has been compromised.">
<meta property="og:description" content="Have I Been Pwned allows you to search across multiple data breaches to see if your email address or phone number has been compromised." />
<meta property="og:url" content="https://haveibeenpwned.com/Passwords" />
<meta property="og:image" content="https://haveibeenpwned.com/Content/Images/SocialLogo.png" />
<meta property="fb:app_id" content="553845121487108" />
<link href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous" />
<link rel="alternate" type="application/rss+xml" title="Have I Been Pwned latest breaches" href="https://feeds.feedburner.com/HaveIBeenPwnedLatestBreaches" />
<link href="/content/css/pwned?v=TJpFHTnWbCdnvZpFZNcpTl8bplj6lOPz2G1FK2yI8bU1" rel="stylesheet" />
<link href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous" />
<link rel="shortcut icon" href="/favicon.ico">
<script type="text/javascript" nonce="UhJPPJDq4jk7mD/HZZNx">
      (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'
    ] = r; i[r
    ] = i[r
    ] || function () {
          (i[r
        ].q = i[r
        ].q || []).push(arguments)
    }, i[r
    ].l = 1 * new Date(); a = s.createElement(o),
          m = s.getElementsByTagName(o)[
        0
    ]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
})(window, document, 'script', ' //www.google-analytics.com/analytics.js', 'ga');
      ga('create', 'UA-45816011-1', 'haveibeenpwned.com');
      ga('send', 'pageview');
    </script>
<script type="text/javascript" nonce="UhJPPJDq4jk7mD/HZZNx">
        var appInsights=window.appInsights||function(config)
        {
            function r(config){ t[config
        ] = function(){ var i = arguments; t.queue.push(function(){ t[config
                ].apply(t, i)
            })
        }
    }
            var t = { config:config
    },u=document,e=window,o='script',s=u.createElement(o),i,f;for(s.src=config.url||' //az416426.vo.msecnd.net/scripts/a/ai.0.js',u.getElementsByTagName(o)[0].parentNode.appendChild(s),t.cookie=u.cookie,t.queue=[],i=['Event','Exception','Metric','PageView','Trace','Ajax'];i.length;)r('track'+i.pop());return r('setAuthenticatedUserContext'),r('clearAuthenticatedUserContext'),config.disableExceptionTracking||(i='onerror',r('_'+i),f=e[i],e[i]=function(config, r, u, e, o) { var s = f && f(config, r, u, e, o); return s !== !0 && t['_' + i](config, r, u, e, o),s}),t
}({
            instrumentationKey:'9744aaee-21f7-42b6-95b2-8ebc0f2bcfeb'
});
        
        window.appInsights=appInsights;
        appInsights.trackPageView();
    </script>
</head>
<body>
<div class="bodyGradient">
<header class="navbar navbar-inverse navbar-static-top">
<div class="container">
<div class="navbar-header">
<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a href="/" class="navbar-brand">';--</a>
</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav navbar-right">
<li><a href="/">Home</a></li>
<li><a href="/NotifyMe" class="notifyOfPwning" data-toggle="modal" data-target="#notifyMeModal" data-remote="false">Notify me</a></li>
<li><a href="/DomainSearch">Domain search</a></li>
<li><a href="/PwnedWebsites">Who's been pwned</a></li>
<li class="active"><a href="/Passwords">Passwords</a></li>
<li class="dropdown ">
<a href="#" class="dropdown-toggle" data-toggle="dropdown">API</a>
<ul class="dropdown-menu">
<li><a href="/API/v3">Overview</a></li>
<li><a href="/API/Key">API key</a></li>
<li><a href="/API/TermsOfUse">Terms of use</a></li>
</ul>
</li>
<li class="dropdown ">
<a href="#" class="dropdown-toggle" data-toggle="dropdown">About</a>
<ul class="dropdown-menu">
<li><a href="/About">Who, what &amp; why</a></li>
<li><a href="/Privacy">Privacy</a></li>
<li><a href="/FAQs">FAQs</a></li>
<li><a href="/Pastes">Pastes</a></li>
<li><a href="/OptOut">Opt-out</a></li>
<li><a href="https://twitter.com/haveibeenpwned" rel="noopener">Twitter</a></li>
<li><a href="https://www.facebook.com/haveibeenpwned/">Facebook</a></li>
<li><a rel="me" href="https://infosec.exchange/@haveibeenpwned">Mastodon</a></li>
<li><a href="https://haveibeenpwned.uservoice.com/" rel="noopener">Suggest a feature</a></li>
<li><a href="http://feeds.feedburner.com/HaveIBeenPwnedLatestBreaches" rel="noopener"><i class="fa fa-rss"></i> Breaches</a></li>
</ul>
</li>
<li><a href="/Donate">Donate <i class="fa fa-bitcoin"></i> <i class="fa fa-paypal payPalLogo"></i></a></li>
</ul>
</div>
</div>
</header>
<div class="main">
<div class="container">
<h1>Pwned Passwords</h1>
<p>
Pwned Passwords are hundreds of millions of real world passwords previously exposed in data breaches.
This exposure makes them unsuitable for ongoing use as they're at much greater risk of being
used to take over other accounts. They're searchable online below as well as being
downloadable for use in other online systems. <a href="https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2#cloudflareprivacyandkanonymity">Read more about how HIBP protects the privacy of searched passwords</a>.
</p>
<noscript>
      <p class="alert alert-danger">
        You've disabled JavaScript! If you submit a password in the form below, it will not be
        anonymised first.
      </p>
    </noscript>
</div>
</div>
<div id="searchContainer" class="secondaryHeader">
<div class="container">
<form action="/Passwords" method="post" novalidate="novalidate">
<div class="input-group">
<input autocapitalize="off" autocorrect="off" class="form-control" data-val="true" data-val-maxlength="The field Password must be a string or array type with a maximum length of &#39;450&#39;." data-val-maxlength-max="450" data-val-minlength="The field Password must be a string or array type with a minimum length of &#39;1&#39;." data-val-minlength-min="1" id="Password" maxlength="450" name="Password" placeholder="password" spellcheck="false" type="password" />
<span class="input-group-btn">
<button class="btn btn-primary btn-lg" type="submit" id="searchPwnedPasswords">pwned?</button>
</span>
</div>
<div class="progress progress-striped active" id="loading">
<div class="progress-bar" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
</div>
</div>
</form>
</div>
</div>
<div class="tertiaryHeader panel-collapse in">
<div class="container">
<p>
<img src="/Content/Images/PasswordManager/1PasswordLogo.svg" alt="1Password Logo" />
<span>Generate secure, unique passwords for every account</span>
<a href="https://1password.com/" target="_blank" class="btn btn-group-xs" rel="noopener">Learn more at 1Password.com</a>
</p>
<p class="why1Password"><a href="/1Password">Why 1Password?</a></p>
</div>
</div>
</div>
<div id="invalidAccount" class="pwnedSearchResult panel-collapse  collapse ">
<div class="container">
<div class="row pwnResultBanner">
<h2>
</h2>
</div>
</div>
</div>
<div id="noPwnage" class="pwnedSearchResult panel-collapse  collapse">
<div class="container">
<div class="row pwnResultBanner">
<div class="pwnTitle">
<h2>Good news &mdash; no pwnage found!</h2>
<p>
This password wasn't found in any of the Pwned Passwords loaded into Have I Been Pwned.
That doesn't necessarily mean it's a <em>good</em> password, merely that it's not indexed
on this site. If you're not already using a password manager, go and download 1Password
and change all your passwords to be strong and unique.
</p>
</div>
<div class="actionsBar clearfix">
<div class="row">
<div class="col-sm-8 stepsToBetterSecurity">
<img src="/Content/Images/PasswordManager/1PasswordLogo.svg" alt="1Password Logo" />
<h3>3 Steps to better security</h3>
</div>
<div class="col-sm-4 startUsingPasswordManager">
<a href="https://1password.com/haveibeenpwned/" target="_blank" class="btn btn-group-sm passwordManagerLink" rel="noopener">Start using 1Password.com</a>
</div>
</div>
<div class="row passwordManagerSteps">
<div class="col-sm-4">
<p>
<a href="https://1password.com/haveibeenpwned/" target="_blank" class="passwordManagerLink" rel="noopener">
<img src="/Content/Images/PasswordManager/Step1.png" alt="Step 1" class="passwordManagerStep" /><br />
<strong>Step 1</strong> Protect yourself using 1Password to generate and save strong passwords for each website.
</a>
</p>
</div>
<div class="col-sm-4">
<p>
<a href="https://1password.com/haveibeenpwned/" target="_blank" class="passwordManagerLink" rel="noopener">
<img src="/Content/Images/PasswordManager/Step2.png" alt="Step 2" class="passwordManagerStep" /><br />
<strong>Step 2</strong> Enable 2 factor authentication and store the codes inside your 1Password account.
</a>
</p>
</div>
<div class="col-sm-4">
<p>
<a href="/NotifyMe" class="notifyOfPwning" data-toggle="modal" data-target="#notifyMeModal" data-remote="false">
<img src="/Content/Images/PasswordManager/Step3.png" alt="Step 3" class="passwordManagerStep" /><br />
<strong>Step 3</strong> <span class="subscribe">Subscribe</span> to notifications for any other breaches. Then just change that unique password.
</a>
</p>
</div>
</div>
<div class="row why1Password">
<div class="col-sm-12">
<p><a href="/1Password">Why 1Password?</a></p>
</div>
</div>
</div>
<p class="socialLinks clearfix">
<a class="socialLink" href="https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fhaveibeenpwned.com" rel="noopener"><i class="fa fa-facebook-square"></i></a>
<a class="socialLink" href="https://twitter.com/intent/tweet?url=https%3a%2f%2fhaveibeenpwned.com&amp;text=Good+news+%e2%80%94+I+haven%27t+been+pwned!+%40haveibeenpwned" rel="noopener"><i class="fa fa-twitter-square"></i></a>
<a href="/Donate" class="socialLink"><i class="fa fa-bitcoin bitcoinLogo"></i><i class="fa fa-paypal payPalLogo"></i> Donate</a>
</p>
</div>
</div>
</div>
<div id="pwnedWebsitesContainer">
<div id="pwnedWebsiteBanner" class="pwnedSearchResult pwnedRow panel-collapse collapse">
<div class="container">
<div class="row pwnResultBanner">
<div class="pwnTitle">
<h2>
Oh no &mdash; pwned!
</h2>
<h3 id="pwnedPasswordResult">This password has been seen before</h3>
<p>
This password has previously appeared in a data breach and should never be used. If
you've ever used it anywhere before, change it!
</p>
</div>
<div class="actionsBar clearfix">
<div class="row">
<div class="col-sm-8 stepsToBetterSecurity">
<img src="/Content/Images/PasswordManager/1PasswordLogo.svg" alt="1Password Logo" />
<h3>3 Steps to better security</h3>
</div>
<div class="col-sm-4 startUsingPasswordManager">
<a href="https://1password.com/haveibeenpwned/" target="_blank" class="btn btn-group-sm passwordManagerLink" rel="noopener">Start using 1Password.com</a>
</div>
</div>
<div class="row passwordManagerSteps">
<div class="col-sm-4">
<p>
<a href="https://1password.com/haveibeenpwned/" target="_blank" class="passwordManagerLink" rel="noopener">
<img src="/Content/Images/PasswordManager/Step1.png" alt="Step 1" class="passwordManagerStep" /><br />
<strong>Step 1</strong> Protect yourself using 1Password to generate and save strong passwords for each website.
</a>
</p>
</div>
<div class="col-sm-4">
<p>
<a href="https://1password.com/haveibeenpwned/" target="_blank" class="passwordManagerLink" rel="noopener">
<img src="/Content/Images/PasswordManager/Step2.png" alt="Step 2" class="passwordManagerStep" /><br />
<strong>Step 2</strong> Enable 2 factor authentication and store the codes inside your 1Password account.
</a>
</p>
</div>
<div class="col-sm-4">
<p>
<a href="/NotifyMe" class="notifyOfPwning" data-toggle="modal" data-target="#notifyMeModal" data-remote="false">
<img src="/Content/Images/PasswordManager/Step3.png" alt="Step 3" class="passwordManagerStep" /><br />
<strong>Step 3</strong> <span class="subscribe">Subscribe</span> to notifications for any other breaches. Then just change that unique password.
</a>
</p>
</div>
</div>
<div class="row why1Password">
<div class="col-sm-12">
<p><a href="/1Password">Why 1Password?</a></p>
</div>
</div>
</div>
<p class="socialLinks clearfix">
<a class="socialLink" href="https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fhaveibeenpwned.com" rel="noopener"><i class="fa fa-facebook-square"></i></a>
<a class="socialLink" href="https://twitter.com/intent/tweet?url=https%3a%2f%2fhaveibeenpwned.com&amp;text=Oh+no+%e2%80%94+I%27ve+been+pwned!+%40haveibeenpwned" rel="noopener"><i class="fa fa-twitter-square"></i></a>
<a href="/Donate" class="socialLink"><i class="fa fa-bitcoin bitcoinLogo"></i><i class="fa fa-paypal payPalLogo"></i> Donate</a>
</p>
</div>
</div>
</div>
</div>
<div class="container" id="PwnedPasswords">
<h3>Password reuse and credential stuffing</h3>
<p>
Password reuse is normal. It's extremely risky, but it's so common because it's easy and
people aren't aware of the potential impact. Attacks such as <a href="https://www.troyhunt.com/password-reuse-credential-stuffing-and-another-1-billion-records-in-have-i-been-pwned/">credential stuffing</a>
take advantage of reused credentials by automating login attempts against systems using known
emails and password pairs.
</p>
<hr />
<h3>NIST's guidance: check passwords against those obtained from previous data breaches</h3>
<p>
The Pwned Passwords service was created in August 2017 after <a href="https://www.nist.gov/itl/tig/special-publication-800-63-3">
NIST released guidance specifically recommending that user-provided passwords be checked
against existing data breaches
</a>. The rationale for this advice and suggestions for how
applications may leverage this data is described in detail in the blog post titled
<a href="https://www.troyhunt.com/introducing-306-million-freely-downloadable-pwned-passwords/">Introducing 306 Million Freely Downloadable Pwned Passwords</a>.
In February 2018, <a href="https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2">version 2 of the service was released</a>
with more than half a billion passwords, each now also with a count of how many times they'd
been seen exposed. <a href="https://www.troyhunt.com/pwned-passwords-v3-is-now-live">A version 3 release in July 2018</a>
contributed a further 16M passwords, <a href="https://www.troyhunt.com/the-773-million-record-collection-1-data-reach">version 4 came in January 2019</a>
along with the &quot;Collection #1&quot; data breach to bring the total to over 551M.
<a href="https://www.troyhunt.com/pwned-passwords-version-5">Version 5 landed in July 2019</a>
with a total count of 555M records, <a href="https://www.troyhunt.com/pwned-passwords-version-6">version 6 arrived June 2020</a>
with almost 573M then <a href="https://www.troyhunt.com/inside-the-cit0day-breach-collection">version 7 arrived November 2020</a>
bringing the total passwords to over 613M. The final monolithic release was <a href="https://www.troyhunt.com/open-source-pwned-passwords-with-fbi-feed-and-225m-new-nca-passwords-is-now-live">version 8 in December 2021</a>
which marked the beginning of the ingestion pipeline utilised by law enforcement agencies such as the FBI.
</p>
<hr />
<h3>Downloading the Pwned Passwords list</h3>
<p>
As of May 2022, the best way to get the most up to date passwords is to use <a href="https://github.com/HaveIBeenPwned/PwnedPasswordsDownloader">the Pwned Passwords downloader</a>.
The downloaded password hashes may be integrated into other systems and used to verify
whether a password has previously appeared in a data breach after which a system may warn the
user or even block the password outright. For suggestions on integration practices,
<a href="https://www.troyhunt.com/introducing-306-million-freely-downloadable-pwned-passwords/">read the Pwned Passwords launch blog post</a>
for more information.
</p>
<hr />
<h3>Cloudflare's support</h3>
<p>
The costs of providing this service for free would be extensive were it not for
<a href="https://www.cloudflare.com/" rel="noopener">Cloudflare's'</a> support. They provide
the resources to ensure more than 99% of all queries are served directly from their
infrastructure by aggressively caching the data at their edge nodes over and beyond what
would normally be freely available. Their support in making this data available to help
organisations protect their customers is most appreciated.
</p>
<p align="center">
<a href="https://www.cloudflare.com/" rel="noopener" id="Cloudflare"><img src="/Content/Images/CloudflareLogo.svg" alt="Cloudflare logo" /></a>
</p>
</div>
<div class="modal fade" id="notifyMeModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
<h4 class="modal-title">Notify me</h4>
</div>
<div class="modal-body" id="notifyMeContainer">
<div class="panel-collapse in" id="notifySubmission">
<form action="/NotifyMe" id="notifyMeForm" method="post" role="form"> <p>
Get notified when future pwnage occurs and your account is compromised.
</p>
<div class="form-group row">
<div class="col-lg-7">
<input class="form-control" data-val="true" data-val-maxlength="The field Email must be a string or array type with a maximum length of &#39;255&#39;." data-val-maxlength-max="255" data-val-regex="That doesn&#39;t look like a valid email address" data-val-regex-pattern="^(?!^.{256})[^\x00-\x1F\*\x7F]+@[^\x00-\x1F\*\x7F]+$" data-val-required="Can&#39;t do much without an email address" id="NotifyEmail" maxlength="255" name="NotifyEmail" placeholder="enter your email address" type="email" value="" />
</div>
</div>
<div class="form-group row">
<script src="https://www.google.com/recaptcha/api.js" async defer></script>
<div class="g-recaptcha" data-sitekey="6Lcb0woTAAAAAJAbo3ToF_yAJMKMsZgSATbQTRmI"></div>
</div>
<div class="validation-summary-valid alert alert-danger" data-valmsg-summary="true" id="notifyError"><ul><li style="display:none"></li>
</ul></div> <div class="form-group row" id="notificationSubmitRow">
<input type="submit" value="notify me of pwnage" class="btn btn-primary" /><i class="fa fa-3x fa-cog fa-spin fa-loader" id="notificationLoading" style="display: none;"></i>
</div>
</form>
</div>
<div class="panel-collapse collapse" id="notifySuccess">
<p>
You've just been sent a verification email, all you need to do now is confirm your
address by clicking on the link when it hits your mailbox and you'll be automatically
notified of future pwnage. In case it doesn't show up, check your junk mail and if
you <em>still</em> can't find it, you can always repeat this process.
</p>
<hr />
<p class="text-center" id="postNotificationCallsToAction">
<a class="btn btn-primary" id="addAnotherNotification">add another address</a>
<a class="socialLink" href="https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fhaveibeenpwned.com" rel="noopener"><i class="fa fa-facebook-square fa-3x"></i></a>
<a class="socialLink" href="https://twitter.com/intent/tweet?url=https%3a%2f%2fhaveibeenpwned.com&amp;text=Have%20you%20been%20pwned%3F%20Get%20told%20when%20you%20are%20with%20a%20free%20%40haveibeenpwned%20subscription" rel="noopener"><i class="fa fa-twitter-square fa-3x"></i></a>
</p>
</div>
</div>
</div>
</div>
</div>
<footer>
<div class="container text-center">
<hr />
<p>
<a href="https://www.troyhunt.com" rel="noopener">A troyhunt.com project</a>
</p>
<p>
<a href="https://www.facebook.com/troyahunt" rel="noopener"><i class="fa fa-facebook-square fa-3x"></i></a>
<a href="https://twitter.com/troyhunt" rel="noopener"><i class="fa fa-twitter-square fa-3x"></i></a>
<a href="https://www.troyhunt.com/contact/" rel="noopener"><i class="fa fa-envelope fa-3x"></i></a>
</p>
</div>
</footer>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js" integrity="sha384-rY/jv8mMhqDabXSo+UCggqKtdmBfd3qC2/KvyTDNQ6PcUJXaxK1tMepoQda4g5vB" crossorigin="anonymous"></script>
<script nonce="UhJPPJDq4jk7mD/HZZNx">(window.jQuery) || document.write('<script src="/scripts/jquery"></script>');</script>
<script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<script nonce="UhJPPJDq4jk7mD/HZZNx">($.fn.modal) || document.write('<script src="/scripts/bootstrap"></script>');</script>
<script src="/scripts/pwned?v=J5kDtegTTfifrl5ICQPwX-M-ueHzPbNnOOkVCelICf41"></script>
<script src="/scripts/passwordsearch?v=8oLMrdym_kXHYVnzd0-cVqvcv10j3OyKB3qExq3jxrg1"></script>
<script nonce="UhJPPJDq4jk7mD/HZZNx">(function(){var js = "window['__CF$cv$params']={r:'7cf3e4587b972838',m:'0H6Sq.5gmu6put6IgMN91vaJkHKjR_bdE8VYBLvQP4s-1685417358-0-AcdWkA2rweDt8SM0e3VgRbRNh369/xhM7myzUF3OfpLn',u:'/cdn-cgi/challenge-platform/h/b'};_cpo=document.createElement('script');_cpo.nonce='UhJPPJDq4jk7mD/HZZNx',_cpo.src='/cdn-cgi/challenge-platform/scripts/invisible.js',document.getElementsByTagName('head')[0].appendChild(_cpo);";var _0xh = document.createElement('iframe');_0xh.height = 1;_0xh.width = 1;_0xh.style.position = 'absolute';_0xh.style.top = 0;_0xh.style.left = 0;_0xh.style.border = 'none';_0xh.style.visibility = 'hidden';document.body.appendChild(_0xh);function handler() {var _0xi = _0xh.contentDocument || _0xh.contentWindow.document;if (_0xi) {var _0xj = _0xi.createElement('script');_0xj.nonce = 'UhJPPJDq4jk7mD/HZZNx';_0xj.innerHTML = js;_0xi.getElementsByTagName('head')[
                0
            ].appendChild(_0xj);
        }
    }if (document.readyState !== 'loading') {handler();
    } else if (window.addEventListener) {document.addEventListener('DOMContentLoaded', handler);
    } else {var prev = document.onreadystatechange || function () {};document.onreadystatechange = function (e) {prev(e);if (document.readyState !== 'loading') {document.onreadystatechange = prev;handler();
            }
        };
    }
})();</script></body>
</html>
