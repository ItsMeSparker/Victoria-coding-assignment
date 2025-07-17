import doctest
import math

''' 
The Date representation type alias for tuple list contain:
[Year, Month, Day]
'''
Date_tuple_type = tuple[int, int, int]

''' 
The Netflix show representation type alias for tuple list 
[Type, Titles, List of Directors, List of Actors, Date of Realease]
'''
Netflix_show_tuple_type = tuple[str, str, list[str], list[str], Date_tuple_type]

def raise_to_power(li_base: list[int], li_exponant: list[int]):
    """ This function will take 2 list of integer. One as the list of base and
    one as the list of exponant. The argument lists do not need to has the same
    length so this fucntion will calculate the power of the elements
    that share the same index of 2 list then put it back to base list.
    
    >>> li_base = [1,2,3]; raise_to_power(li_base,[2,4]); li_base
    [1, 16, 3]
    >>> li_base = [1,2,3]; raise_to_power(li_base,[2,4,0]); li_base
    [1, 16, 1]
    >>> li_base = [1,2,3]; raise_to_power(li_base,[2,4,0,2]); li_base
    [1, 16, 1]
    >>> li_base = [5,6,7]; raise_to_power(li_base,[]); li_base
    [5, 6, 7]
    >>> li_base = []; raise_to_power(li_base,[2,2,2]); li_base
    []
    """
    i = 0
    while i < len(li_base) and i < len(li_exponant):
        #I use 'while' and 'and' in case they are not the same length
        li_base[i] = pow(li_base[i],li_exponant[i])
        i += 1

def month_int(month: str) -> int:
    """
    This function will be used in create_data function for more simpification.
    it is just take month as string and return month as number.
    """
    if month == 'Jan': return 1
    elif month == 'Feb': return 2
    elif month == 'Mar': return 3
    elif month == 'Apr': return 4
    elif month == 'May': return 5
    elif month == 'Jun': return 6
    elif month == 'Jul': return 7
    elif month == 'Aug': return 8
    elif month == 'Sep': return 9
    elif month == 'Oct': return 10
    elif month == 'Nov': return 11
    elif month == 'Dec': return 12
    
def create_date(Date_str: str) -> list[Date_tuple_type]:
    """ This function will take date as string and will return the return it
    in the form of tuple list of 3 integers for further use in this assignment.
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    >>> create_date('24-Nov-03')
    (2003, 11, 24)
    >>> create_date('01-Nov-24')
    (2024, 11, 1)
    >>> create_date('01-Apr-00')
    (2000, 4, 1)
    >>> create_date('31-Oct-23')
    (2023, 10, 31)
    >>> create_date('25-Dec-17')
    (2017, 12, 25)
    """
    List_date_str = Date_str.split('-')
    
    Day = (int(List_date_str[0]))
    Month = (month_int(List_date_str[1]))
    Year = (2000 + int(List_date_str[2]))
    
    return (Year, Month, Day)

def create_show(Type: str, Title: str, Directors: str, Actors: str,\
                Date_str: str) -> list[Netflix_show_tuple_type]:
    """ This function will take 5 string as the Netflix show infomation and will 
    be returned in the form of tuple list that we create in the top of the file.
    
    >>> create_show('Movie', 'Audrey & Daisy', 'Bonni Cohen:Jon Shenk', \
    '', '23-Sep-16') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Audrey & Daisy', ['Bonni Cohen', 'Jon Shenk'], [], (2016, 9, 23))
    
    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David \
    Walliams:Timothy Spall', '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
     ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
      'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
     (2019, 7, 1))
     
     >>> create_show('Movie', 'Blank Movie', '', '', '01-Sep-00')
     ('Movie', 'Blank Movie', [], [], (2000, 9, 1))
     
     >>> create_show('Documentary', 'Rizzler and the wild skibidy', \
     'Baby Gronk:The Rizzler', 'Ryan Gosling:Logan Paul:Mr. Beast', \
     '22-Jul-14') # doctest: +NORMALIZE_WHITESPACE
     ('Documentary', 'Rizzler and the wild skibidy', ['Baby Gronk', \
     'The Rizzler'], ['Ryan Gosling', 'Logan Paul', 'Mr. Beast'], (2014, 7, 22))
    """
    
    if Directors: Directors_list = Directors.split(':')
    else: Directors_list = []
    
    if Actors: Actors_list = Actors.split(':')
    else: Actors_list = []
    
    Date = create_date(Date_str)
    
    return (Type, Title, Directors_list, Actors_list, Date)

def get_titles(Netflix_show_list: list[Netflix_show_tuple_type]) -> list[str]:
    """ This function will take the tuple list of Netflix show and will return
    the list of all the titles in the taken tuple list.
    
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
     (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'],\
     (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
     ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
      'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
     (2019, 12, 31))]
    
    >>> get_titles(loshows)
    ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']
    
    >>> RizzlerShows = [\
    ('Documentary', 'Rizzler and the wild skibidy', ['Baby Gronk',\
    'The Rizzler'], ['Ryan Gosling', 'Logan Paul', 'Mr. Beast'],\
    (2014, 7, 22)), \
    ('Movie', 'Still Water and the Mango', ['Pod Arnon'], ['Livvy Dunn', \
    'Elon Musk', 'Donald Trump'], (2015, 8, 2)),\
    ('TV Show', 'The Lost Lunchly', ['Mr. Beast', 'Logan Paul', 'KSI'], \
    ['Baruk Obama', 'Baby Gronk', 'Ryan Gosling'], (2077, 9, 24))]
    
    >>> get_titles(RizzlerShows) # doctest: +NORMALIZE_WHITESPACE
    ['Rizzler and the wild skibidy', 'Still Water and the Mango',\
    'The Lost Lunchly']
    """
    titles_list = []
    for i in range(len(Netflix_show_list)):
        titles_list.append(Netflix_show_list[i][1])
        
    return titles_list

def is_actor_in_show(Netflix_show: Netflix_show_tuple_type, \
                     Actor_name: str) -> bool: #take just one tuple, not a list.
    """ This function will take one Netflix show tuple and a string name of
    an actor. This function will indicate if that certain actor is in this
    Netflix show or not.
    
    >>> is_actor_in_show(('Movie', 'Blank Movie', [], [], (2000, 9, 1)), \
    'Joe Biden')
    False
    
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Justin Bieber')
    False
    
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
     'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
     'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Michael Cera')
    True
    
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
     'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
     'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'MichaEL cerA')
    True
    
    >>> is_actor_in_show(('Documentary', 'Rizzler and the wild skibidy',\
    ['Baby Gronk', 'The Rizzler'], ['Ryan Gosling', 'Logan Paul', 'Mr. Beast'],\
    (2014, 7, 22)), 'ryAn goSLing')
    True
    
    >>> is_actor_in_show(('TV Show', 'The Lost Lunchly', ['Mr. Beast', \
    'Logan Paul', 'KSI'], ['Baruk Obama', 'Baby Gronk', 'Ryan Gosling'],\
    (2077, 9, 24)), 'ChrIS eveN')
    False
    """
    for Actor in Netflix_show[3]:
        if Actor_name.upper() == Actor.upper(): 
            return True
            
    return False

def count_shows_before_date(Netflix_show_list: list[Netflix_show_tuple_type],\
                             Date: list[Date_tuple_type]) -> int:
    """ This function will take a list of Netflix show tuple and date to count
    how many show that release before that specific date.
    
    >>> RizzlerShows = [\
    ('Documentary', 'Rizzler and the wild skibidy', ['Baby Gronk',\
    'The Rizzler'], ['Ryan Gosling', 'Logan Paul', 'Mr. Beast'],\
    (2014, 7, 22)), \
    ('Movie', 'Still Water and the Mango', ['Pod Arnon'], ['Livvy Dunn', \
    'Elon Musk', 'Donald Trump'], (2015, 8, 2)),\
    ('TV Show', 'The Lost Lunchly', ['Mr. Beast', 'Logan Paul', 'KSI'], \
    ['Baruk Obama', 'Baby Gronk', 'Ryan Gosling'], (2077, 9, 24))]
    
    >>> count_shows_before_date(RizzlerShows, (2011, 3, 19))
    0
    >>> count_shows_before_date(RizzlerShows, (2099, 12, 25))
    3
    >>> count_shows_before_date(RizzlerShows, (2022, 5, 9))
    2
    
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
     (2017, 2, 6)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'],\
     (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
     ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
      'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
     (2017, 4, 18))]
    
    >>> count_shows_before_date(loshows, (2015, 1, 1))
    0
    >>> count_shows_before_date(loshows, (2018, 10, 20))
    3
    >>> count_shows_before_date(loshows, (2024, 11, 3))
    4
    """
    Movies_before = 0 
    
    for i in range(len(Netflix_show_list)):
        if Date[0] > Netflix_show_list[i][4][0]: #Chack by Year
            Movies_before += 1
        elif Date[0] == Netflix_show_list[i][4][0]: #If equal year
            if Date[1] > Netflix_show_list[i][4][1]: #Chaeck by month
                Movies_before += 1
            elif Date[1] == Netflix_show_list[i][4][1]: #If equal month
                if Date[2] > Netflix_show_list[i][4][2]: #Check by day
                    Movies_before += 1
    return Movies_before

def get_shows_with_actor(Netflix_show_list: list[Netflix_show_tuple_type],\
                         Actor_name: str) -> list[Netflix_show_tuple_type]:
    """
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
     (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'], \
     (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
     ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
      'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
     (2019, 12, 31))]
    
    >>> get_shows_with_actor(loshows, 'Jonah Hill')  \
    # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'], \
     (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21))]
    
    >>> get_shows_with_actor(loshows, 'jonaH hiLL')  \
    # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'], \
     (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21))]
    
    >>> get_shows_with_actor(loshows, 'Justin Bieber')
    []
    
    >>> RizzlerShows = [\
    ('Documentary', 'Rizzler and the wild skibidy', ['Baby Gronk',\
    'The Rizzler'], ['Ryan Gosling', 'Logan Paul', 'Mr. Beast'],\
    (2014, 7, 22)), \
    ('Movie', 'Still Water and the Mango', ['Pod Arnon'], ['Livvy Dunn', \
    'Elon Musk', 'Donald Trump'], (2015, 8, 2)),\
    ('TV Show', 'The Lost Lunchly', ['Mr. Beast', 'Logan Paul', 'KSI'], \
    ['Baruk Obama', 'Baby Gronk', 'Ryan Gosling'], (2077, 9, 24))]
    
    >>> get_shows_with_actor(RizzlerShows, 'rYan gOSling') \
    # doctest: +NORMALIZE_WHITESPACE
    [('Documentary', 'Rizzler and the wild skibidy', ['Baby Gronk', \
    'The Rizzler'], ['Ryan Gosling', 'Logan Paul', 'Mr. Beast'], \
    (2014, 7, 22)), ('TV Show', 'The Lost Lunchly', ['Mr. Beast', \
    'Logan Paul', 'KSI'], ['Baruk Obama', 'Baby Gronk', 'Ryan Gosling'], \
    (2077, 9, 24))]
    
    >>> get_shows_with_actor(RizzlerShows, 'bABy gROnK') \
    # doctest: +NORMALIZE_WHITESPACE
    [('TV Show', 'The Lost Lunchly', ['Mr. Beast', 'Logan Paul', 'KSI'], \
    ['Baruk Obama', 'Baby Gronk', 'Ryan Gosling'], (2077, 9, 24))]
    
    >>> get_shows_with_actor(RizzlerShows, 'Not Exist')
    []
    """
    Show_with_the_actor = []
    
    for show in Netflix_show_list:
        if is_actor_in_show(show, Actor_name):
            Show_with_the_actor.append(show)
    return Show_with_the_actor