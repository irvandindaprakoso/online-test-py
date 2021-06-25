public static function format_duration($seconds) {

        $results = [];

        if ($seconds == 0){
            $results[] = "now";
        }

        if ($seconds >= 31536000 ){
            $years = (int) floor($seconds / 31536000);
            $yearString = $years > 1 ? 'years' : 'year';
            $results[] = "$years $yearString";
            $seconds = $seconds % 31536000;
        }

        if ($seconds >= 86400 ){
            $days = (int) floor($seconds / 86400);
            $dayString = $days > 1 ? 'days' : 'day';
            $results[] = "$days $dayString";
            $seconds = $seconds % 86400;
        }

        if ($seconds >= 3600 ){
            $hours = (int) floor($seconds / 3600);
            $hourString = $hours > 1 ? 'hours' : 'hour';
            $results[] = "$hours $hourString";
            $seconds = $seconds % 3600;
        }

        if ($seconds >= 60 && $seconds < 3600){
            $minutes = (int)floor($seconds / 60);
            $minuteString = $minutes > 1 ? 'minutes' : 'minute';
            $results[] = "$minutes $minuteString";
            $seconds = $seconds % 60;
        }

        if ($seconds < 60 && $seconds > 0){
            $secondString = $seconds > 1 ? 'seconds' : 'second';
            $results[] = "$seconds $secondString";
        }

        $last = array_slice($results, - 1);
        $first = implode(', ', array_slice($results, 0, - 1));
        $both = array_filter(array_merge([$first], $last), 'strlen');

        return implode(' and ', $both);
    }
