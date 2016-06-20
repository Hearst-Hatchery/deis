package logger

import (
	"bytes"
	"fmt"

	"github.com/Sirupsen/logrus"
)

// StdOutFormatter formats log messages from the router component.
type StdOutFormatter struct {
}

// Format rewrites a log entry for stdout as a byte array.
func (f *StdOutFormatter) Format(entry *logrus.Entry) ([]byte, error) {
	b := &bytes.Buffer{}
	fmt.Fprintf(b, "%s\n", entry.Message)
	return b.Bytes(), nil
}
